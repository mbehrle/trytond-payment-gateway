# The COPYRIGHT file at the top level of this repository
# contains the full copyright notices and license terms.
from trytond.pool import PoolMeta, Pool

__all__ = ['PartyErase']


class PartyErase:
    __metaclass__ = PoolMeta
    __name__ = 'party.erase'

    def to_erase(self, party_id):
        pool = Pool()
        PaymentProfile = pool.get('party.payment_profile')

        to_erase = super(PartyErase, self).to_erase(party_id)
        to_erase += [
            (PaymentProfile, [('party', '=', party_id)], True,
                ['name', 'provider_reference', 'last_4_digits', 'expiry_month',
                    'expiry_year'],
                [None, '****' , '****', '01', '2000']),
            ]
        return to_erase
