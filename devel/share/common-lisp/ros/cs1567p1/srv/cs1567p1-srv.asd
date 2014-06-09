
(cl:in-package :asdf)

(defsystem "cs1567p1-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MakeNewMaze" :depends-on ("_package_MakeNewMaze"))
    (:file "_package_MakeNewMaze" :depends-on ("_package"))
    (:file "GetMazeWall" :depends-on ("_package_GetMazeWall"))
    (:file "_package_GetMazeWall" :depends-on ("_package"))
    (:file "ConstantCommand" :depends-on ("_package_ConstantCommand"))
    (:file "_package_ConstantCommand" :depends-on ("_package"))
  ))