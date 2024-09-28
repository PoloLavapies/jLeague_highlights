python3 j_highlights.py $1 $2
ls *.mp4 > files_tmp.txt
python3 mk_files.py
ffmpeg -f concat -safe 0 -i files.txt -c copy "J$1ハイライト.mp4"
ls 【公式】ハイライト* > files_to_delete.txt
python3 mk_delete_command.py
chmod u+x file_delete.sh
./file_delete.sh
rm file_delete.sh
rm files_to_delete.txt
rm files_tmp.txt
rm files.txt