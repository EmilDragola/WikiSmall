#!/bin/bash

zenity --question --title=Напоминание --ok-label=Ok --cancel-label=Отложить --text="$*"

case $? in 
  0)
  ;; 
  1) ~/remindme/remind.py "Через 15 минут" "$*"
  ;; 
esac