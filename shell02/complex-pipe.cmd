$ grep 'Title' spells.txt | sort | uniq -c | sort -n -r | head -10 > popular_spells.txt
