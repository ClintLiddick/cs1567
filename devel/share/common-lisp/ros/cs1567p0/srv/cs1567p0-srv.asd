
(cl:in-package :asdf)

(defsystem "cs1567p0-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "ConstantCommand" :depends-on ("_package_ConstantCommand"))
    (:file "_package_ConstantCommand" :depends-on ("_package"))
  ))