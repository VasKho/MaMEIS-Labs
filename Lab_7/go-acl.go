package main

import (
    "os"
    "log"
    "flag"
)

func main() {
    var file_path string
    flag.StringVar(&file_path, "path", "./default", "path to created file")
    flag.Parse()

    newFile, err := os.Create(file_path)
    if err != nil {
        log.Fatal(err)
    }
    log.Println(newFile.Name())
    newFile.Close()

    err = os.Chown(file_path, 0, 0)
    if err != nil {
        log.Fatal(err)
    }

    err = os.Chmod(file_path, 0760)
    if err != nil {
        log.Println(err)
    }

    fileInfo, err := os.Stat(file_path)
    if err != nil {
        log.Fatal(err)
    }
    log.Println(fileInfo.Mode())
}
