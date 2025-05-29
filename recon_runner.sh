echo "enter target domain or ip: "
read  target
# generate output filename with timestamp
filename = "logs/recon_$(date + %y-%m-%d_%h-%M-%s).txt"
#  run your recon script and log output
python3 recon.py "$target" | tee "$filename"
# Add and commit the result
cd logs
git add "$(basename  "$filename")"
git commit -m "recon result for $target at $(date)"
git push
