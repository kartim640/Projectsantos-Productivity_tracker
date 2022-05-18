# Version 2.0
import tkinter
import tkinter as tk
from tkinter import ttk
import json
from datetime import datetime as dt
from tkinter import messagebox

# Layout

root = tk.Tk()
root.geometry('500x250')
root.title('Santos R2 Tracking version 2.0')
root.resizable(0, 0)

# Labels of widget
ttk.Label(root, text='Tracking Json Generator', foreground='Black', font=('aria', 15, 'bold')).grid(column=0, row=1, sticky=tk.NE)
ttk.Label(root, text="Tracking ID :", font=("Times New Roman", 10)).grid(column=0, row=5, sticky=tk.W, padx=20, pady=10)
ttk.Label(root, text="Carrier Code :", font=("Times New Roman", 10)).grid(column=0, row=6, sticky=tk.W, padx=20, pady=10)
ttk.Label(root, text="Event Type :", font=("Times New Roman", 10)).grid(column=0, row=7, sticky=tk.W, padx=20, pady=10)
ttk.Label(root, text="Events :", font=("Times New Roman", 10)).grid(column=0, row=8, sticky=tk.W, padx=20, pady=10)

# Input Tracking ID
trackingid_var = tk.StringVar()
trackingid_entry = ttk.Entry(root, width=30, textvariable=trackingid_var)
trackingid_entry.grid(column=1, row=5)

# Combobox Carrier Code
carriercode_var = tk.StringVar()
carriercode_entry = ttk.Combobox(root, width=27, textvariable=carriercode_var)
carriercode_entry['values'] = ('fedex', 'usps', 'ups')
carriercode_entry.current(0)
carriercode_entry.grid(column=1, row=6)
carriercode_entry.current()

# Combobox type of event
eventtype_var = tk.StringVar()
eventtype_entry = ttk.Combobox(root, width=27, textvariable=eventtype_var)
eventtype_entry['values'] = ('Live', '14 days before', '45 days before')
eventtype_entry.current(0)
eventtype_entry.grid(column=1, row=7)
eventtype_entry.current()

# Combobox Events
events_var = tk.StringVar()
events_entry = ttk.Combobox(root, width=27)
events_entry['values'] = ('Shipped',
                          'On the way',
                          'On Hold',
                          'Delayed',
                          'Held at Customs',
                          'Available for pickup',
                          'Out for Delivery',
                          'Delivery attempted',
                          'Held for Pickup in Carrier location',
                          'Cancelled',
                          'Undeliverable',
                          'Lost',
                          'Delivered',
                          'Expired')
events_entry.current(0)
events_entry.grid(column=1, row=8)
events_entry.current()


def click():
    # Converting Human readable Date & Time to Timestamp
    normaltime = int(dt.timestamp(dt.now()))
    epoachlivetime = normaltime * 1000
    timechange = epoachlivetime

    # Type of event Time Choosing
    if eventtype_entry.get() == "live":
        timechange = epoachlivetime
    elif eventtype_entry.get() == "14 days before":
        timechange = (epoachlivetime - 1209600000)
    elif eventtype_entry.get() == "45 days before":
        timechange = (epoachlivetime - 3888000000)



    shipped = {"trackingId": trackingid_entry.get(),  # Filling the Dict by auto input from the text entry field
               "carrierCode": carriercode_entry.get(),
               "code": "INFO_RECEIVED",
               "subCode": "INFO_RECEIVED_001",
               "estimatedDeliveryTimestamp": timechange + 18000000,
               "updatedTimestamp": timechange,
               "eventsList": [
                   {
                       "location": {
                           "city": "hyd",
                           "country": "IND",
                           "landmark": "random",
                           "state": "ts",
                           "zipCode": "500001"
                       },
                       "status": {
                           "code": "INFO_RECEIVED",
                           "subCode": "INFO_RECEIVED_001",
                           "details": "Order Placed",
                           "statusTimestamp": timechange
                       }
                   }
               ]
               }

    on_the_way = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "IN_TRANSIT",
        "subCode": "IN_TRANSIT_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    on_hold = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "CUSTOMER_ACTION",
        "subCode": "CUSTOMER_ACTION_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 120000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "CUSTOMER_ACTION",
                    "subCode": "CUSTOMER_ACTION_001",
                    "details": "Package on hold",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    delayed = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "DELAYED",
        "subCode": "DELAYED_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELAYED",
                    "subCode": "DELAYED_001",
                    "details": "Package delay",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    held_at_customs = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "DELAYED",
        "subCode": "DELAYED_002",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELAYED",
                    "subCode": "DELAYED_002",
                    "details": "Package is Held at customs",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    available_for_pickup = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "AVAILABLE_FOR_PICKUP",
        "subCode": "AVAILABLE_FOR_PICKUP_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package is Shipped",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "AVAILABLE_FOR_PICKUP",
                    "subCode": "AVAILABLE_FOR_PICKUP_001",
                    "details": "Available for Pickup",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    out_for_delivery = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "OUT_FOR_DELIVERY",
        "subCode": "OUT_FOR_DELIVERY_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    delivery_attempted = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "DELIVERY_ATTEMPTED",
        "subCode": "DELIVERY_ATTEMPTED_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempt",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    held_for_pickup_in_carrier_location = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "AVAILABLE_FOR_PICKUP",
        "subCode": "AVAILABLE_FOR_PICKUP_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempted",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "AVAILABLE_FOR_PICKUP",
                    "subCode": "AVAILABLE_FOR_PICKUP_001",
                    "details": "Package is held for Pickup at carrier location",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    cancelled = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "EXCEPTION",
        "subCode": "EXCEPTION_008",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 3000000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempted",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "AVAILABLE_FOR_PICKUP",
                    "subCode": "AVAILABLE_FOR_PICKUP_001",
                    "details": "Package is Available for Pickup",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "EXCEPTION",
                    "subCode": "EXCEPTION_008",
                    "details": "Order Cancelled",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    undeliverable = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "UNDELIVERABLE",
        "subCode": "UNDELIVERABLE_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempt",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "UNDELIVERABLE",
                    "subCode": "UNDELIVERABLE_001",
                    "details": "Package is Undeliverable",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    lost = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "UNDELIVERABLE",
        "subCode": "UNDELIVERABLE_003",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package shipped",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempt",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "UNDELIVERABLE",
                    "subCode": "UNDELIVERABLE_003",
                    "details": "Package is lost",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    delivered = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "DELIVERED",
        "subCode": "DELIVERED_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package shipped",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERED",
                    "subCode": "DELIVERED_001",
                    "details": "Package Delivered",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    expired = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "EXPIRED",
        "subCode": "EXPIRED_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package shipped",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERED",
                    "subCode": "DELIVERED_001",
                    "details": "Package Delivered",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "EXPIRED",
                    "subCode": "EXPIRED_001",
                    "details": "Tracking expired",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    # noinspection PyGlobalUndefined
    def eve():
        global trigger
        if events_entry.get() == 'Shipped':  # Combobox input in Events to pick the JSON
            trigger = shipped
        elif events_entry.get() == 'On the way':
            trigger = on_the_way
        elif events_entry.get() == 'On the way':
            trigger = on_the_way
        elif events_entry.get() == 'On Hold':
            trigger = on_hold
        elif events_entry.get() == 'Delayed':
            trigger = delayed
        elif events_entry.get() == 'Held at Customs':
            trigger = held_at_customs
        elif events_entry.get() == 'Available for pickup':
            trigger = available_for_pickup
        elif events_entry.get() == 'Out for Delivery':
            trigger = out_for_delivery
        elif events_entry.get() == 'Delivery attempted':
            trigger = delivery_attempted
        elif events_entry.get() == 'Held for Pickup in Carrier location':
            trigger = held_for_pickup_in_carrier_location
        elif events_entry.get() == 'Cancelled':
            trigger = cancelled
        elif events_entry.get() == 'Undeliverable':
            trigger = undeliverable
        elif events_entry.get() == 'Lost':
            trigger = lost
        elif events_entry.get() == 'Delivered':
            trigger = delivered
        elif events_entry.get() == 'Expired':
            trigger = expired
        if trackingid_entry.get() == "":
            messagebox.showerror("Tracking ID Error", "Error: Please Enter the Tracking ID")
        else:
            top = tk.Toplevel(root)
            top.geometry("700x500")
            entry = tkinter.Text(top,height=30, bd=3, padx=30, pady=10)
            entry.pack()


            entry.insert(tk.INSERT, json.dumps(trigger, indent=4) )

    eve()


def generate():
    click()

btn = ttk.Button(root, text="Generate", command=generate)
btn.place(x=350, y=200)

root.mainloop()
