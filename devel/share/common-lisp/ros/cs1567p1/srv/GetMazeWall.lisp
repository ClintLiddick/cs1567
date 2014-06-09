; Auto-generated. Do not edit!


(cl:in-package cs1567p1-srv)


;//! \htmlinclude GetMazeWall-request.msg.html

(cl:defclass <GetMazeWall-request> (roslisp-msg-protocol:ros-message)
  ((col
    :reader col
    :initarg :col
    :type cl:integer
    :initform 0)
   (row
    :reader row
    :initarg :row
    :type cl:integer
    :initform 0)
   (direction
    :reader direction
    :initarg :direction
    :type cl:integer
    :initform 0))
)

(cl:defclass GetMazeWall-request (<GetMazeWall-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetMazeWall-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetMazeWall-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cs1567p1-srv:<GetMazeWall-request> is deprecated: use cs1567p1-srv:GetMazeWall-request instead.")))

(cl:ensure-generic-function 'col-val :lambda-list '(m))
(cl:defmethod col-val ((m <GetMazeWall-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cs1567p1-srv:col-val is deprecated.  Use cs1567p1-srv:col instead.")
  (col m))

(cl:ensure-generic-function 'row-val :lambda-list '(m))
(cl:defmethod row-val ((m <GetMazeWall-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cs1567p1-srv:row-val is deprecated.  Use cs1567p1-srv:row instead.")
  (row m))

(cl:ensure-generic-function 'direction-val :lambda-list '(m))
(cl:defmethod direction-val ((m <GetMazeWall-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cs1567p1-srv:direction-val is deprecated.  Use cs1567p1-srv:direction instead.")
  (direction m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetMazeWall-request>) ostream)
  "Serializes a message object of type '<GetMazeWall-request>"
  (cl:let* ((signed (cl:slot-value msg 'col)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'row)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'direction)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetMazeWall-request>) istream)
  "Deserializes a message object of type '<GetMazeWall-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'col) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'row) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'direction) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetMazeWall-request>)))
  "Returns string type for a service object of type '<GetMazeWall-request>"
  "cs1567p1/GetMazeWallRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetMazeWall-request)))
  "Returns string type for a service object of type 'GetMazeWall-request"
  "cs1567p1/GetMazeWallRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetMazeWall-request>)))
  "Returns md5sum for a message object of type '<GetMazeWall-request>"
  "d4865ac0ed82ec40a20774e6e4853f56")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetMazeWall-request)))
  "Returns md5sum for a message object of type 'GetMazeWall-request"
  "d4865ac0ed82ec40a20774e6e4853f56")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetMazeWall-request>)))
  "Returns full string definition for message of type '<GetMazeWall-request>"
  (cl:format cl:nil "int64 col~%int64 row~%int64 direction~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetMazeWall-request)))
  "Returns full string definition for message of type 'GetMazeWall-request"
  (cl:format cl:nil "int64 col~%int64 row~%int64 direction~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetMazeWall-request>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetMazeWall-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GetMazeWall-request
    (cl:cons ':col (col msg))
    (cl:cons ':row (row msg))
    (cl:cons ':direction (direction msg))
))
;//! \htmlinclude GetMazeWall-response.msg.html

(cl:defclass <GetMazeWall-response> (roslisp-msg-protocol:ros-message)
  ((wall
    :reader wall
    :initarg :wall
    :type cl:fixnum
    :initform 0))
)

(cl:defclass GetMazeWall-response (<GetMazeWall-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetMazeWall-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetMazeWall-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cs1567p1-srv:<GetMazeWall-response> is deprecated: use cs1567p1-srv:GetMazeWall-response instead.")))

(cl:ensure-generic-function 'wall-val :lambda-list '(m))
(cl:defmethod wall-val ((m <GetMazeWall-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cs1567p1-srv:wall-val is deprecated.  Use cs1567p1-srv:wall instead.")
  (wall m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetMazeWall-response>) ostream)
  "Serializes a message object of type '<GetMazeWall-response>"
  (cl:let* ((signed (cl:slot-value msg 'wall)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetMazeWall-response>) istream)
  "Deserializes a message object of type '<GetMazeWall-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'wall) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetMazeWall-response>)))
  "Returns string type for a service object of type '<GetMazeWall-response>"
  "cs1567p1/GetMazeWallResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetMazeWall-response)))
  "Returns string type for a service object of type 'GetMazeWall-response"
  "cs1567p1/GetMazeWallResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetMazeWall-response>)))
  "Returns md5sum for a message object of type '<GetMazeWall-response>"
  "d4865ac0ed82ec40a20774e6e4853f56")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetMazeWall-response)))
  "Returns md5sum for a message object of type 'GetMazeWall-response"
  "d4865ac0ed82ec40a20774e6e4853f56")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetMazeWall-response>)))
  "Returns full string definition for message of type '<GetMazeWall-response>"
  (cl:format cl:nil "int8 wall~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetMazeWall-response)))
  "Returns full string definition for message of type 'GetMazeWall-response"
  (cl:format cl:nil "int8 wall~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetMazeWall-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetMazeWall-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GetMazeWall-response
    (cl:cons ':wall (wall msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GetMazeWall)))
  'GetMazeWall-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GetMazeWall)))
  'GetMazeWall-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetMazeWall)))
  "Returns string type for a service object of type '<GetMazeWall>"
  "cs1567p1/GetMazeWall")