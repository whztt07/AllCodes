// AllCodes.cpp:
//

#include "stdafx.h"
#include <gtest/gtest.h>

int _tmain(int argc, _TCHAR* argv[])
{
	testing::InitGoogleTest(&argc, argv);
	setlocale(LC_ALL, "");
	RUN_ALL_TESTS();
    return 0;
}

