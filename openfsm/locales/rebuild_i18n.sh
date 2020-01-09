#!/bin/sh

I18NDOMAIN="opencore"
LOCALES="../../openfsm/locales"
LOGI18NDUDE=$LOCALES/rebuild_i18n.log
POTFILE=$LOCALES/$I18NDOMAIN.pot

rm $LOGI18NDUDE

# find the source, as it shoul be in the source directories
# rebuild pot file for package's domain and merge it with any manual translations needed
echo "Rebuilding POT file $POTFILE..."
i18ndude rebuild-pot --pot $POTFILE \
    --create $I18NDOMAIN \
    ../ || exit 1

# synchronise translations for package's domain
for POFILE in `find $LOCALES -type f -name ${I18NDOMAIN}.po`; do
    echo "Syncing messages to PO file $POFILE..."
    i18ndude sync --pot $POTFILE $POFILE || exit 1
done

echo "Running msgfmt to ensure .mo files are compiled with no syntax issues"
type msgfmt
if [ $? -ne 0 ]; then
    echo "Could not find msgfmt command. Try installing gnu gettext."
    exit 1
else
    for subdir in `find . -name LC_MESSAGES`; do
       echo "  running msgfmt -o $subdir/${I18NDOMAIN}.mo $subdir/${I18NDOMAIN}.po"
       msgfmt -o $subdir/${I18NDOMAIN}.mo $subdir/${I18NDOMAIN}.po
    done
fi

# Report of errors and suspect untranslated messages
echo "\nGetting status of markup in page templates..."

ERRORS=`find ../ -regextype posix-extended -regex '.*\.(pt|html)' | xargs i18ndude find-untranslated | grep -e '^-ERROR' | wc -l`
WARNINGS=`find ../ -regextype posix-extended -regex '.*\.(pt|html)' | xargs i18ndude find-untranslated | grep -e '^-WARN' | wc -l`
FATAL=`find ../ -regextype posix-extended -regex '.*\.(pt|html)' | xargs i18ndude find-untranslated | grep -e '^-FATAL' | wc -l`

echo ""
echo "There are $WARNINGS warnings (possibly missing i18n markup)"
echo "There are $ERRORS errors (almost definitely missing i18n markup)"
echo "There are $FATAL fatal errors (template could not be parsed, eg. if it's not html)"
echo ""
echo "For more details, run 'find ../ -name \"*pt\" | xargs i18ndude find-untranslated' or"
echo "Look the rebuild i18n log generate for this script called 'rebuild_i18n.log' on locales dir"

touch ./$LOGI18NDUDE

find ../ -regextype posix-extended -regex '.*\.(pt|html)' | xargs i18ndude find-untranslated > ./$LOGI18NDUDE
