//
// Generated file, do not edit! Created by nedtool 5.0 from AirFrame.msg.
//

#ifndef __ALOHA_AIRFRAME_M_H
#define __ALOHA_AIRFRAME_M_H

#include <omnetpp.h>

// nedtool version check
#define MSGC_VERSION 0x0500
#if (MSGC_VERSION!=OMNETPP_VERSION)
#    error Version mismatch! Probably this file was generated by an earlier version of nedtool: 'make clean' should help.
#endif


namespace aloha {

/**
 * Class generated from <tt>AirFrame.msg:21</tt> by nedtool.
 * <pre>
 * //
 * // AirFrame packet, contains information about the sender
 * //
 * packet AirFrame
 * {
 *     string senderName;
 *     // TODO Task 3.1.1: Add fields to airframe
 *     //int senderId;
 *     //int pktNum;
 *     //bool isAck;
 *     // end of TODO
 * }
 * </pre>
 */
class AirFrame : public ::omnetpp::cPacket
{
  protected:
    ::omnetpp::opp_string senderName;

  private:
    void copy(const AirFrame& other);

  protected:
    // protected and unimplemented operator==(), to prevent accidental usage
    bool operator==(const AirFrame&);

  public:
    AirFrame(const char *name=nullptr, int kind=0);
    AirFrame(const AirFrame& other);
    virtual ~AirFrame();
    AirFrame& operator=(const AirFrame& other);
    virtual AirFrame *dup() const {return new AirFrame(*this);}
    virtual void parsimPack(omnetpp::cCommBuffer *b) const;
    virtual void parsimUnpack(omnetpp::cCommBuffer *b);

    // field getter/setter methods
    virtual const char * getSenderName() const;
    virtual void setSenderName(const char * senderName);
};

inline void doParsimPacking(omnetpp::cCommBuffer *b, const AirFrame& obj) {obj.parsimPack(b);}
inline void doParsimUnpacking(omnetpp::cCommBuffer *b, AirFrame& obj) {obj.parsimUnpack(b);}

} // namespace aloha

#endif // ifndef __ALOHA_AIRFRAME_M_H

