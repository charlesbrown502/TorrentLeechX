if [[ -n $RCLONE_CONFIG ]]; then
 echo "Rclone config detected"
 echo -e "$RCLONE_CONFIG" > /app/rclone.conf
fi

python3 update.py && bash setup.sh; python3 -m tobrot
