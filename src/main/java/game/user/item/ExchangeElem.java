/*
 * This file is part of OrionAlpha, a MapleStory Emulator Project.
 * Copyright (C) 2018 Eric Smith <notericsoft@gmail.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
package game.user.item;

import common.item.ItemAccessor;
import common.item.ItemSlotBase;

/**
 *
 * @author Eric
 * @author sunnyboy
 */
public class ExchangeElem {

    public boolean add;
    public Add a;
    public Remove r;

    public ExchangeElem() {
        this.a = new Add();
        this.r = new Remove();
    }

    public boolean isAdd() {
        return add;
    }

    public void setAdd(boolean add) {
        this.add = add;
    }

    public Add getAdd() {
        return a;
    }

    public void setAdd(Add a) {
        this.a = a;
    }

    public Remove getRemove() {
        return r;
    }

    public void setRemove(Remove r) {
        this.r = r;
    }

    public static class Add {

        public int itemID;
        public short count;
        public ItemSlotBase item;

        public int getItemID() {
            return itemID;
        }

        public void setItemID(int itemID) {
            this.itemID = itemID;
        }

        public short getCount() {
            return count;
        }

        public void setCount(short count) {
            this.count = count;
        }

        public ItemSlotBase getItem() {
            return item;
        }

        public void setItem(ItemSlotBase item) {
            this.item = item;
        }
    }

    public static class Remove {

        public int itemID;
        public short count;
        public byte ti;
        public short pos;

        public int getItemID() {
            return itemID;
        }

        public void setItemID(int itemID) {
            this.itemID = itemID;
        }

        public short getCount() {
            return count;
        }

        public void setCount(short count) {
            this.count = count;
        }

        public byte getTI() {
            return ti;
        }

        public void setTI(byte ti) {
            this.ti = ti;
        }

        public short getPOS() {
            return pos;
        }

        public void setPOS(short pos) {
            this.pos = pos;
        }
    }

    public boolean initAdd(int itemID, short count, ItemSlotBase item) {
        this.add = true;
        this.a.itemID = itemID;
        this.a.count = count;
        this.a.item = item;
        if (item != null) {
            itemID = item.getItemID();
            count = item.getItemNumber();
        }
        if (ItemAccessor.isBundleTypeIndex(ItemAccessor.getItemTypeIndexFromID(itemID))) {
            if (ItemAccessor.isRechargeableItem(itemID)) {
                if (count > 2000) {
                    return false;
                }
            } else {
                if (ItemInfo.getBundleItem(itemID).getSlotMax() < count) {
                    return false;
                }
            }
        }
        return true;
    }
}
