$(document).ready(function() {
	$('.salonsSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  infinite: true,
	  prevArrow: $('.salons .leftArrow'),
	  nextArrow: $('.salons .rightArrow'),
	  responsive: [
	    {
	      breakpoint: 991,
	      settings: {
	        
	      	centerMode: true,
  			//centerPadding: '60px',
	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});
	$('.servicesSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.services .leftArrow'),
	  nextArrow: $('.services .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {
	        

	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {
	        
	      	centerMode: true,
  			//centerPadding: '60px',
	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	$('.mastersSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.masters .leftArrow'),
	  nextArrow: $('.masters .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {
	        

	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {
	        

	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	$('.reviewsSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.reviews .leftArrow'),
	  nextArrow: $('.reviews .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {
	        

	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {
	        

	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	// menu
	$('.header__mobMenu').click(function() {
		$('#mobMenu').show()
	})
	$('.mobMenuClose').click(function() {
		$('#mobMenu').hide()
	})

	let appointmentState = {
		salon: null,
		category: null,
		service: null,
		master: null,
		date: null,
		time: null,
	}
	const datetimeSection = $('#time')
	const serviceSection = $('#service')
	const confirmSection = $('#confirm')
	const datetimeSectionTitle = $('.time__title')
	const datepickerContainer = $('#datepicker__container')
	const timepickerContainer = $('#timepicker__container')
	const serviceNextBtn = $('.time__btns_next')
	const serviceBackBtn = $('.serviceFinallys__form_back')

	const getFormattedDate = (date) => {
		const months = {
			0: 'января',
			1: 'февраля',
			2: 'марта',
			3: 'апреля',
			4: 'мая',
			5: 'июня',
			6: 'июля',
			7: 'августа',
			8: 'сентября',
			9: 'октября',
			10: 'ноября',
			11: 'декабря',
		}

		return `${date.getDate()} ${months[date.getMonth()]}`
	}

	const finallySalonName = $('.serviceFinally__form_header__service')
	const finallySalonAddress = $('.serviceFinally__form_header__address')
	const finallyServiceName = $('.serviceFinally__form_content__title')
	const finallyServicePrice = $('.serviceFinally__form_content__price')
	const finallyMasterName = $('.accordion__block_master')
	const finallyTime = $('.serviceFinally__form_content__time')
	const finallyDate = $('.serviceFinally__form_content__date')

	const updateConfirmSection = () => {
		finallySalonName.text(appointmentState.salon.name)
		finallySalonAddress.text(appointmentState.salon.address)
		finallyServiceName.text(appointmentState.service.name)
		finallyServicePrice.text(`${appointmentState.service.price} ₽`)
		finallyMasterName.text(appointmentState.master.name)
		finallyTime.text(appointmentState.time)
		finallyDate.text(getFormattedDate(appointmentState.date.dateObj))
	}

	const loadData = (url, data={}) => {
		return $.ajax({
			type: 'GET',
			url,
			data,
			headers: { 'X-CSRFToken': getCookie('csrftoken') },
			dataType: 'json',
			async: false
		}).responseJSON
	}

	$('#serviceFinally__form').submit(function(e) {

		const form = $(this)
		form.find('[name=procedure]').val(appointmentState.service.id)
		form.find('[name=employee]').val(appointmentState.master.id)
		form.find('[name=salon]').val(appointmentState.salon.id)
		form.find('[name=appointment_hour]').val(appointmentState.time)
		form.find('[name=date]').val(appointmentState.date.formattedDate)
		form.trigger('submit')
	})

	$(document).on('click', '.close', function(e) {
		$(this).parent().fadeOut();
	})

	$(document).on('click', '#submit_appointment_btn', function(e) {
		e.preventDefault()
		if (!serviceNextBtn.hasClass('active')) { return }

		serviceSection.hide()
		datetimeSection.hide()
		updateConfirmSection()
		confirmSection.show()
	})

	$(document).on('click', '.time__elems_btn', function(e) {
		const timeBtn = $(this)
		$('.time__elems_btn').removeClass('active')
		timeBtn.addClass('active')
		appointmentState.time = timeBtn.data('time')
		serviceNextBtn.addClass('active')
	})

	$(document).on('click', '.serviceFinallys__form_back', function(e) {
		e.preventDefault()
		confirmSection.hide()
		serviceSection.show()
		datetimeSection.show()
	})

	const getDatepickerMinDate = () => {
		const now = new Date();
		return  (now.getHours() < 20) ? now : now.setDate(now.getDate() + 1)
	}

	const buildTimeBlock = (title, times) => {
		const timeBtns = times.map((time) => `<button data-time="${time}" class="time__elems_btn">${time}</button>`).join('')
		return $(`
			<div class="time__items">
				<div class="time__elems_intro">${title}</div>
				<div class="time__elems_elem fic">
					${timeBtns}
				</div>
			</div>
		`)
	}

	const renderTime = (timeSections) => {
		const blockTitles = {
			morning: 'Утро',
			afternoon: 'День',
			evening: 'Вечер'
		}

		const timeBlocks = Object.entries(timeSections).map(([timeSection, times]) => {
			if (times.length === 0) {
				return ''
			}
			return buildTimeBlock(blockTitles[timeSection], times)
		})


		timepickerContainer.empty()
		if (timeBlocks.every((block) => block === '')) {
			timepickerContainer.append($('<div class="time_elemes">Нет мест для записи.</div>'))

		} else {
			const timeItemsContainer = $(`<div class="time__elems"></div>`).append(timeBlocks)
			timepickerContainer.append(timeItemsContainer)
		}


	}

	const weekdays = ['Mo', 'Tu', 'We', 'Td', 'Fr', 'Sa', 'Su']

	const sortTimes = (times) => (
		times
			.map((time) => parseInt(time.split(':')[0]))
			.reduce((acc, hour) => {
				const formatTime = (hour) => `${hour}:00`

				if (hour < 12) {
					return {...acc, morning: [...acc.morning, formatTime(hour)]}
				} else if (hour < 18) {
					return {...acc, afternoon: [...acc.afternoon, formatTime(hour)]}
				} else {
					return {...acc, evening: [...acc.evening, formatTime(hour)]}
				}
			}, {morning: [], afternoon: [], evening: []})

	)


	const datepicker = new AirDatepicker(
		'#datepickerHere',
		{
			language: 'ru',
			dateFormat: 'yyyy/mm/dd',
			multipleDates: false,
			minDate: getDatepickerMinDate(),

			onSelect: function onSelect({ date }) {
				const weekday = weekdays[date.getUTCDay()]
				const day = date.getDate()
				const month = date.getMonth() + 1
				const year = date.getFullYear()
				const formattedDate = `${year}-${month}-${day}`

				const times = loadData(
					'/api/get_available_time',
					{
						salon_id: appointmentState.salon.id,
						master_id: appointmentState.master.id,
						weekday,
						day,
						month,
						date: formattedDate,
					}
				)

				appointmentState = { ...appointmentState, date: { dateObj: date, formattedDate }, time: null}
				serviceNextBtn.removeClass('active')
				renderTime(sortTimes(times))
				timepickerContainer.show()
			},
		},
	)

	$(document).on('click', '.accordion', function(e) {
		e.preventDefault()
		const accordion = e.target
		accordion.classList.toggle("active");
		const panel = $(accordion).next()
		panel.toggleClass('active')
		panel.hasClass('active') ? panel.show() : panel.hide()
		serviceNextBtn.removeClass('active')
	})

	$(document).on('click', '.accordion__master_block', function(e) {
		e.preventDefault()

		const masterDiv = $(this)
		const masterIntro = masterDiv.find('.accordion__block_intro')
		const masterName = masterIntro.text()
		const masterId = masterIntro.data('master_id')

		appointmentState = {
			...appointmentState,
			master: {
				id: masterId,
				name: masterName,
			}
		}


		const accordion_btn = masterDiv.parent().parent().find('> button.accordion')
		accordion_btn.addClass('selected').text(masterName)
		accordion_btn.trigger('click')
		if (appointmentState.date !== null) {
			$('.air-datepicker-cell.-day-.-selected-').removeClass('-selected-')
		}
		datetimeSection.show()
		timepickerContainer.hide()
	})

	const buildMaster = (master) => {
		return $(`<div class="accordion__block accordion__master_block fic">
					<div class="accordion__block_intro" data-master_id="${master.id}">${master.name} ${master.surname}</div>
				</div>`)
	}

	const renderMasters = (data) => {
		const accordionBtn = $('<button class="accordion">(Выберите мастера)</button>')
		const masters = data.map(buildMaster)
		const masters_wrapper = $('<div class="panel"></div>').append(masters)


		const masters_block = $(`<div class="service__form_block service__masters"></div>`).append(
			accordionBtn,
			masters_wrapper
		)

		$('.dropdowns_container').append(masters_block)
	}

	$(document).on('click', '.accordion__service_block', function(e) {
		e.preventDefault()
		const serviceDiv = $(this)
		const serviceDropdown = serviceDiv.parent().parent().parent().parent()
		const serviceName = serviceDiv.find('.accordion__block_item_intro').text()

		const serviceId = serviceDiv.data('service_id')
		const servicePrice = serviceDiv.data('service_price')
		const categoryName = serviceDiv.data('category_name')
		const categoryId = serviceDiv.data('category_id')

		appointmentState = {
			...appointmentState,
			category: {
				name: categoryName,
				id: categoryId,
			},
			service: {
				name: serviceName,
				id: serviceId,
				price: servicePrice,
			},
			master: null,
			date: null,
			time: null,
		}


		serviceDropdown.nextAll('.service__form_block').remove()
		renderMasters(
			loadData(
				'/api/masters',
				{
					salon_id: appointmentState.salon.id,
					category_id: appointmentState.category.id,
				}
			)
		)

		const accordion_btn = serviceDropdown.find('> button.active')
		accordion_btn.addClass('selected').text(serviceName)
		accordion_btn.trigger('click')
		datetimeSectionTitle.text('Выберите дату')
		datepickerContainer.show()
	})

	const buildService = (service, categoryName, categoryId) => {
		return $(`<div 
					class="accordion__block_item accordion__service_block fic"
					data-service_id="${service.id}"
					data-service_price="${service.price}"
					data-category_name="${categoryName}"
					data-category_id="${categoryId}"
					>
					<div class="accordion__block_item_intro">${service.name}</div>
					<div class="accordion__block_item_address">${service.price} ₽</div>
				</div>`)
	}

	const buildCategory = (category) => {
		const services = category.services.map((service) => buildService(service, category.name, category.id))
		const category_div = $(`
			<button class="accordion" data-category_id="${category.id}">${category.name}</button>
			<div class="panel">
				<div class="accordion__block_items">
				</div>
			</div>	
		`)

		category_div.find('.accordion__block_items').append(services)
		return category_div
	}

	const renderServices = (data) => {
		const accordionBtn = $('<button class="accordion">(Выберите услугу)</button>')
		const categories = data.map(buildCategory)
		const categories_html = $('<div class="panel"></div>').append(categories)


		const categories_block = $(`<div class="service__form_block service__services"></div>`).append(
			accordionBtn,
			categories_html
		)

		categories_block.find('.service__services').append(categories_html)
		$('.dropdowns_container').append(categories_block)
	}

	$('.accordion__salon_block').on('click', function(e) {
		e.preventDefault()

		const salonDiv = $(this)
		const salonDropdown = salonDiv.parent().parent()
		const salonName = salonDiv.find('.accordion__block_intro').text()
		const salonAddress = salonDiv.find('.accordion__block_address').text()

		appointmentState = {
			...appointmentState,
			salon: {
				id: salonDiv.data('salon_id'),
				name: salonName,
				address: salonAddress,
			},
			service: null,
			master: null,
			time: null,
			date: null,
		}

		salonDropdown.nextAll('.service__form_block').remove()
		renderServices(loadData('/api/categories'))

		const accordion_btn = salonDropdown.find('> button.accordion.active')
		accordion_btn.addClass('selected').text(salonName)
		accordion_btn.click()
		datetimeSection.hide()
	})

	$('.accordion__service_block').on('click', function(e) {
		e.preventDefault()

		const serviceDiv = $(this)
		const serviceName = serviceDiv.find('.accordion__block_intro').text()

		serviceDiv.parent().parent().parent().parent().find('> button.active').addClass('selected').text(serviceName)
		serviceDiv.parent().parent().parent().parent().find('> .panel').hide()
	})


	//popup
	$('.header__block_auth').click(function(e) {
		e.preventDefault()
		$('#authModal').arcticmodal();

		// $('#confirmModal').arcticmodal();

	})

	$('.rewiewPopupOpen').click(function(e) {
		e.preventDefault()
		$('#reviewModal').arcticmodal();
	})
	$('.payPopupOpen').click(function(e) {
		e.preventDefault()
		$('#paymentModal').arcticmodal();
	})
	$('.tipsPopupOpen').click(function(e) {
		e.preventDefault()
		$('#tipsModal').arcticmodal();
	})

	function getCookie(name) {
    	let cookieValue = null;
    	if (document.cookie && document.cookie !== '') {
    	    const cookies = document.cookie.split(';');
    	    for (let i = 0; i < cookies.length; i++) {
    	        const cookie = cookies[i].trim();
    	        // Does this cookie string begin with the name we want?
    	        if (cookie.substring(0, name.length + 1) === (name + '=')) {
    	            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
    	            break;
    	        }
    	    }
    	}
    	return cookieValue;
	}

	$('.tipsPopup__form_inputNum').keyup(function(e) {
		if (this.value.length !== this.maxLength) { return }

		const next = $(this).data('next')
		$(`input[name=num${next}]`).focus()
	})

	function post_request(url, data, success_handler, fail_handler) {
		$.ajax({
			type: 'POST',
			url: url,
			headers: { 'X-CSRFToken': getCookie('csrftoken') },
			data,
			dataType: 'json',
			success: success_handler,
			error: fail_handler
		})

	}


	function clearConfirmationForm() {
		$('.tipsPopup__form_inputNum').each(function(_, inputEl) {
			$(inputEl).val('');
		});
	}

	function clearFormErrors(form) {
		form.find('.field_errors').each(function(_, errorDiv) {
			$(errorDiv).text('')
		})
	}

	$('.authPopup__form').submit(function(e) {
		e.preventDefault();

		const form = $(this);
		const phonenumber = form.find('input[name=tel]').val();
		const confirm_rules = form.find('input[name=confirm_rules]').is(':checked');
		const url = form.attr('action')

		localStorage.setItem('phonenumber', phonenumber);

		const payload = JSON.stringify({ phonenumber, confirm_rules });

		const success_handler = () => {
			clearFormErrors(form)
			$('#authModal').arcticmodal('close');
			$('#confirmModal').arcticmodal();
		}

		const error_handler = (data) => {
			const response = data.responseJSON
			Object.entries(response).forEach(([field, errors]) => {
				const error_list = errors.map((error) => `<li>${error}</li>`).join('');
				const error_block = `<ul>${error_list}</ul>`;
				$(`#${field}__error`).html(error_block);
			})
		}

		post_request(url, payload, success_handler, error_handler)

		return false
	})

	$('.confirmPopup__changeNumber').click(function(e) {
		e.preventDefault();

		clearConfirmationForm();
		clearFormErrors($('.confirmPopup__form'))
		$('#confirmModal').arcticmodal('close');
		$('#authModal').arcticmodal()
	})

	$('#request_code_again').click(function(e) {
		e.preventDefault();

		const confirmForm = $('.confirmPopup__form')
		const url = $('.authPopup__form').attr('action')
		const data = JSON.stringify({
			phonenumber: localStorage.getItem('phonenumber'),
			confirm_rules: true,
		});

		const success_handler = () => {
			clearConfirmationForm();
			clearFormErrors(confirmForm)
			$('.code_sent_notify').show().delay(1000).fadeOut();
		}

		const error_handler = (data) => {
			clearFormErrors(confirmForm)
			const response = data.responseJSON
			Object.entries(response).forEach(([field, errors]) => {
				const error_list = errors.map((error) => `<li>${error}</li>`).join('');
				const error_block = `<ul>${error_list}</ul>`;
				$(`#confirm_registration__error`).html(error_block);
			})
		};

		post_request(url, data, success_handler, error_handler);
	})

	$('.confirmPopup__form').submit(function(e) {
		e.preventDefault();

		const form = $(this)
		const url =form.attr('action')
		const digits = []
		form.find('.tipsPopup__form_inputNum').each(function() {
			digits.push($(this).val())
		})
		const code = parseInt(digits.join(''))
		const data = JSON.stringify({ phonenumber: localStorage.getItem('phonenumber'), code })

		const success_handler = () => {
			$('#confirmModal').arcticmodal('close');
			window.location.replace(window.location.href);
		}
		const error_handler = (data) => {
			const response = data.responseJSON
			Object.entries(response).forEach(([field, errors]) => {
				const error_list = errors.map((error) => `<li>${error}</li>`).join('');
				const error_block = `<ul>${error_list}</ul>`;
				$('#confirm_registration__error').html(error_block);
			})
		}

		post_request(url, data, success_handler, error_handler);
		return false
	})

	//service
	$('.time__items .time__elems_elem .time__elems_btn').click(function(e) {
		e.preventDefault()
		$('.time__elems_btn').removeClass('active')
		$(this).addClass('active')
	})

	$(document).on('click', '.servicePage', function() {
		if($('.time__items .time__elems_elem .time__elems_btn').hasClass('active') && $('.service__form_block > button').hasClass('selected')) {
			$('.time__btns_next').addClass('active')
		}
	})
})
