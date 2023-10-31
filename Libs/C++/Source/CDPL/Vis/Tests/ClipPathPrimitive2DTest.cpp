/* 
 * ClipPathPrimitive2DTest.cpp 
 *
 * This file is part of the Chemical Data Processing Toolkit
 *
 * Copyright (C) 2003 Thomas Seidel <thomas.seidel@univie.ac.at>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program; see the file COPYING. If not, write to
 * the Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
 */


#include <cstddef>

#include <boost/test/auto_unit_test.hpp>

#include "CDPL/Config.hpp"
#include "CDPL/Vis/ClipPathPrimitive2D.hpp"
#include "CDPL/Vis/PathPrimitive2D.hpp"
#include "CDPL/Vis/Rectangle2D.hpp"
#include "CDPL/Vis/Pen.hpp"
#include "CDPL/Vis/Brush.hpp"
#include "CDPL/Vis/Color.hpp"

#ifdef HAVE_CAIRO 
# ifdef HAVE_CAIRO_PNG_SUPPORT

# include <cairo.h>

# include "CDPL/Vis/CairoPointer.hpp"
# include "CDPL/Vis/CairoRenderer2D.hpp"

# endif // HAVE_CAIRO_PNG_SUPPORT
#endif // HAVE_CAIRO


namespace
{

    void checkClone(const CDPL::Vis::ClipPathPrimitive2D& prim)
    {
        using namespace CDPL;
        using namespace Vis;

        GraphicsPrimitive2D::SharedPointer gp_clone_ptr = prim.clone();
        const ClipPathPrimitive2D* prim_clone_ptr = static_cast<const ClipPathPrimitive2D*>(gp_clone_ptr.get());

        BOOST_CHECK_EQUAL(prim_clone_ptr->isEmpty(), prim.isEmpty());
    }
}


BOOST_AUTO_TEST_CASE(ClipPathPrimitive2DTest)
{
    using namespace CDPL;
    using namespace Vis;

    ClipPathPrimitive2D cpp;

    checkClone(cpp);

    cpp.moveTo(10.0, 10.0);
 
    checkClone(cpp);

//-----

#ifdef HAVE_CAIRO 
# ifdef HAVE_CAIRO_PNG_SUPPORT

    CairoPointer<cairo_surface_t> surf_ptr(cairo_image_surface_create(CAIRO_FORMAT_ARGB32, 600, 500));

    BOOST_CHECK(cairo_surface_status(surf_ptr.get()) == CAIRO_STATUS_SUCCESS);

    CairoPointer<cairo_t> ctxt_ptr(cairo_create(surf_ptr.get()));

    BOOST_CHECK(cairo_status(ctxt_ptr.get()) == CAIRO_STATUS_SUCCESS);

    CairoRenderer2D renderer(ctxt_ptr);

    Pen test_pens[] = {
        Pen(Color::BLACK, 0.0, Pen::NO_LINE, Pen::ROUND_CAP, Pen::MITER_JOIN),
        Pen(Color::BLACK, 0.5, Pen::SOLID_LINE, Pen::ROUND_CAP, Pen::BEVEL_JOIN),
        Pen(Color::BLACK, 0.5, Pen::DASH_LINE, Pen::ROUND_CAP, Pen::ROUND_JOIN),
        Pen(Color::BLACK, 0.5, Pen::DOT_LINE, Pen::ROUND_CAP, Pen::MITER_JOIN),
        Pen(Color::BLACK, 0.5, Pen::DASH_DOT_LINE, Pen::ROUND_CAP, Pen::BEVEL_JOIN),
        Pen(Color::BLACK, 0.5, Pen::DASH_DOT_DOT_LINE, Pen::ROUND_CAP, Pen::ROUND_JOIN),
        
        Pen(Color::RED, 1.0, Pen::NO_LINE, Pen::FLAT_CAP, Pen::BEVEL_JOIN),
        Pen(Color::RED, 1.0, Pen::SOLID_LINE, Pen::FLAT_CAP, Pen::ROUND_JOIN),
        Pen(Color::RED, 1.0, Pen::DASH_LINE, Pen::FLAT_CAP, Pen::MITER_JOIN),
        Pen(Color::RED, 1.0, Pen::DOT_LINE, Pen::FLAT_CAP, Pen::BEVEL_JOIN),
        Pen(Color::RED, 1.0, Pen::DASH_DOT_LINE, Pen::FLAT_CAP, Pen::ROUND_JOIN),
        Pen(Color::RED, 1.0, Pen::DASH_DOT_DOT_LINE, Pen::FLAT_CAP, Pen::MITER_JOIN),
        
        Pen(Color::GREEN, 1.5, Pen::NO_LINE, Pen::SQUARE_CAP, Pen::ROUND_JOIN),
        Pen(Color::GREEN, 1.5, Pen::SOLID_LINE, Pen::SQUARE_CAP, Pen::MITER_JOIN),
        Pen(Color::GREEN, 1.5, Pen::DASH_LINE, Pen::SQUARE_CAP, Pen::BEVEL_JOIN),
        Pen(Color::GREEN, 1.5, Pen::DOT_LINE, Pen::SQUARE_CAP, Pen::ROUND_JOIN),
        Pen(Color::GREEN, 1.5, Pen::DASH_DOT_LINE, Pen::SQUARE_CAP, Pen::MITER_JOIN),
        Pen(Color::GREEN, 1.5, Pen::DASH_DOT_DOT_LINE, Pen::SQUARE_CAP, Pen::BEVEL_JOIN),
        
        Pen(Color::BLUE, 2.0, Pen::NO_LINE, Pen::ROUND_CAP, Pen::MITER_JOIN),
        Pen(Color::BLUE, 2.0, Pen::SOLID_LINE, Pen::ROUND_CAP, Pen::BEVEL_JOIN),
        Pen(Color::BLUE, 2.0, Pen::DASH_LINE, Pen::ROUND_CAP, Pen::ROUND_JOIN),
        Pen(Color::BLUE, 2.0, Pen::DOT_LINE, Pen::ROUND_CAP, Pen::MITER_JOIN),
        Pen(Color::BLUE, 2.0, Pen::DASH_DOT_LINE, Pen::ROUND_CAP, Pen::BEVEL_JOIN),
        Pen(Color::BLUE, 2.0, Pen::DASH_DOT_DOT_LINE, Pen::ROUND_CAP, Pen::ROUND_JOIN),
    
        Pen(Color::MAGENTA, 3.0, Pen::NO_LINE, Pen::FLAT_CAP, Pen::BEVEL_JOIN),
        Pen(Color::MAGENTA, 3.0, Pen::SOLID_LINE, Pen::FLAT_CAP, Pen::ROUND_JOIN),
        Pen(Color::MAGENTA, 3.0, Pen::DASH_LINE, Pen::FLAT_CAP, Pen::MITER_JOIN),
        Pen(Color::MAGENTA, 3.0, Pen::DOT_LINE, Pen::FLAT_CAP, Pen::BEVEL_JOIN),
        Pen(Color::MAGENTA, 3.0, Pen::DASH_DOT_LINE, Pen::FLAT_CAP, Pen::ROUND_JOIN),
        Pen(Color::MAGENTA, 3.0, Pen::DASH_DOT_DOT_LINE, Pen::FLAT_CAP, Pen::MITER_JOIN),
        
        Pen(Color::CYAN, 5.0, Pen::NO_LINE, Pen::SQUARE_CAP, Pen::ROUND_JOIN),
        Pen(Color::CYAN, 5.0, Pen::SOLID_LINE, Pen::SQUARE_CAP, Pen::MITER_JOIN),
        Pen(Color::CYAN, 5.0, Pen::DASH_LINE, Pen::SQUARE_CAP, Pen::BEVEL_JOIN),
        Pen(Color::CYAN, 5.0, Pen::DOT_LINE, Pen::SQUARE_CAP, Pen::ROUND_JOIN),
        Pen(Color::CYAN, 5.0, Pen::DASH_DOT_LINE, Pen::SQUARE_CAP, Pen::MITER_JOIN),
        Pen(Color::CYAN, 5.0, Pen::DASH_DOT_DOT_LINE, Pen::SQUARE_CAP, Pen::BEVEL_JOIN),
        
        Pen(Color(1.0, 1.0, 0.0, 0.5), 10.0, Pen::NO_LINE, Pen::ROUND_CAP, Pen::MITER_JOIN),
        Pen(Color(1.0, 1.0, 0.0, 0.5), 10.0, Pen::SOLID_LINE, Pen::ROUND_CAP, Pen::BEVEL_JOIN),
        Pen(Color(1.0, 1.0, 0.0, 0.5), 10.0, Pen::DASH_LINE, Pen::ROUND_CAP, Pen::ROUND_JOIN),
        Pen(Color(1.0, 1.0, 0.0, 0.5), 10.0, Pen::DOT_LINE, Pen::ROUND_CAP, Pen::MITER_JOIN),
        Pen(Color(1.0, 1.0, 0.0, 0.5), 10.0, Pen::DASH_DOT_LINE, Pen::ROUND_CAP, Pen::BEVEL_JOIN),
        Pen(Color(1.0, 1.0, 0.0, 0.5), 10.0, Pen::DASH_DOT_DOT_LINE, Pen::ROUND_CAP, Pen::ROUND_JOIN)
    };

    Brush test_brushes[] = {
        Brush(Color::RED, Brush::SOLID_PATTERN),
        Brush(Color(1.0, 1.0, 1.0, 0.5), Brush::DENSE1_PATTERN),
        Brush(Color::BLUE, Brush::DENSE2_PATTERN),
        Brush(Color::YELLOW, Brush::DENSE3_PATTERN),
        Brush(Color::MAGENTA, Brush::DENSE4_PATTERN),
        Brush(Color::WHITE, Brush::DENSE5_PATTERN),
        Brush(Color::GREEN, Brush::DENSE6_PATTERN),
        Brush(Color::CYAN, Brush::DENSE7_PATTERN),
        Brush(Color::DARK_MAGENTA, Brush::H_PATTERN),
        Brush(Color::DARK_GREEN, Brush::V_PATTERN),
        Brush(Color::DARK_BLUE, Brush::CROSS_PATTERN),
        Brush(Color::DARK_YELLOW, Brush::LEFT_DIAG_PATTERN),
        Brush(Color::DARK_CYAN, Brush::RIGHT_DIAG_PATTERN),
        Brush(Color::DARK_RED, Brush::DIAG_CROSS_PATTERN),
        Brush(Color::BLACK, Brush::NO_PATTERN)
    };

    PathPrimitive2D pp;

    pp.arcTo(12.0, 20.0, 10.0, 10.0, 270.0, 40.0);
    pp.lineTo(60.0, 25.0);
    pp.arcTo(60.0, 35.0, 5.0, 10.0, 270.0, 95.0);
    pp.arcTo(30.0, 40.0, 15.0, 8.0, -20.0, -300.0);
    pp.lineTo(20.0, 30.0);

    cpp.moveTo(50.0, 50.0);
    cpp.lineTo(550.0, 50.0);
    cpp.lineTo(300.0, 450.0);
    cpp.closePath();
    
    Rectangle2D bbox;

    cpp.getBounds(bbox, 0);

    renderer.setPen(Color::RED);
    renderer.setBrush(Brush());
    renderer.drawRectangle(bbox.getMin()(0), bbox.getMin()(1), bbox.getWidth(), bbox.getHeight());
    renderer.setPen(Color::BLACK);
    renderer.drawPath(cpp);
    
    double y = 10.0;

    for (std::size_t i = 0; i < 7; i++, y += 70.0) {
        double x = 10.0;

        for (std::size_t j = 0; j < 6; j++, x += 100.0) {
            if (((i % 2) == 0 && (j % 2) != 0) || ((i % 2) != 0 && (j % 2) == 0))
                cpp.render(renderer);
            else
                ClipPathPrimitive2D().render(renderer);
            
            pp.setPen(test_pens[i * 6 + j]);
            pp.setBrush(test_brushes[(i * 6 + j) % 15]);

            renderer.saveState();
            renderer.transform({ { 1.0, 0.0, x }, { 0.0, 1.0, y }, { 0.0, 0.0, 1.0 } });

            pp.render(renderer);

            BOOST_CHECK(cairo_surface_status(surf_ptr.get()) == CAIRO_STATUS_SUCCESS);
            BOOST_CHECK(cairo_status(ctxt_ptr.get()) == CAIRO_STATUS_SUCCESS);

            renderer.restoreState();
        }
    }

    BOOST_CHECK(cairo_surface_write_to_png(surf_ptr.get(), "ClipPathPrimitive2DTest.png") == CAIRO_STATUS_SUCCESS);

# endif // HAVE_CAIRO_PNG_SUPPORT
#endif // HAVE_CAIRO

}

