/* Software License Agreement (BSD License)
 *
 * Copyright (c) 2011, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *  * Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above
 *    copyright notice, this list of conditions and the following
 *    disclaimer in the documentation and/or other materials provided
 *    with the distribution.
 *  * Neither the name of Willow Garage, Inc. nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 * Auto-generated by genmsg_cpp from file /home/clinton/cs1567_ws/src/cs1567p1/srv/GetMazeWall.srv
 *
 */


#ifndef CS1567P1_MESSAGE_GETMAZEWALLREQUEST_H
#define CS1567P1_MESSAGE_GETMAZEWALLREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace cs1567p1
{
template <class ContainerAllocator>
struct GetMazeWallRequest_
{
  typedef GetMazeWallRequest_<ContainerAllocator> Type;

  GetMazeWallRequest_()
    : col(0)
    , row(0)
    , direction(0)  {
    }
  GetMazeWallRequest_(const ContainerAllocator& _alloc)
    : col(0)
    , row(0)
    , direction(0)  {
    }



   typedef int64_t _col_type;
  _col_type col;

   typedef int64_t _row_type;
  _row_type row;

   typedef int64_t _direction_type;
  _direction_type direction;




  typedef boost::shared_ptr< ::cs1567p1::GetMazeWallRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::cs1567p1::GetMazeWallRequest_<ContainerAllocator> const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;

}; // struct GetMazeWallRequest_

typedef ::cs1567p1::GetMazeWallRequest_<std::allocator<void> > GetMazeWallRequest;

typedef boost::shared_ptr< ::cs1567p1::GetMazeWallRequest > GetMazeWallRequestPtr;
typedef boost::shared_ptr< ::cs1567p1::GetMazeWallRequest const> GetMazeWallRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::cs1567p1::GetMazeWallRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::cs1567p1::GetMazeWallRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace cs1567p1

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/hydro/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/hydro/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::cs1567p1::GetMazeWallRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::cs1567p1::GetMazeWallRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cs1567p1::GetMazeWallRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cs1567p1::GetMazeWallRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cs1567p1::GetMazeWallRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cs1567p1::GetMazeWallRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::cs1567p1::GetMazeWallRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0e6bf50cc227007cc10e97fe2f9994b2";
  }

  static const char* value(const ::cs1567p1::GetMazeWallRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0e6bf50cc227007cULL;
  static const uint64_t static_value2 = 0xc10e97fe2f9994b2ULL;
};

template<class ContainerAllocator>
struct DataType< ::cs1567p1::GetMazeWallRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cs1567p1/GetMazeWallRequest";
  }

  static const char* value(const ::cs1567p1::GetMazeWallRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::cs1567p1::GetMazeWallRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 col\n\
int64 row\n\
int64 direction\n\
";
  }

  static const char* value(const ::cs1567p1::GetMazeWallRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::cs1567p1::GetMazeWallRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.col);
      stream.next(m.row);
      stream.next(m.direction);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct GetMazeWallRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::cs1567p1::GetMazeWallRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::cs1567p1::GetMazeWallRequest_<ContainerAllocator>& v)
  {
    s << indent << "col: ";
    Printer<int64_t>::stream(s, indent + "  ", v.col);
    s << indent << "row: ";
    Printer<int64_t>::stream(s, indent + "  ", v.row);
    s << indent << "direction: ";
    Printer<int64_t>::stream(s, indent + "  ", v.direction);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CS1567P1_MESSAGE_GETMAZEWALLREQUEST_H
