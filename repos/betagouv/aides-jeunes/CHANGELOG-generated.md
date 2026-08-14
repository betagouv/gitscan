## Changelog : aides-jeunes (30 derniers jours, au 12 août 2026)

### Résumé
Cette période a été marquée par un important travail de maintenance des données pour garantir la fiabilité des informations proposées. De nombreux liens obsolètes ou dispositifs devenus privés ont été nettoyés. Parallèlement, des correctifs importants ont été apportés au moteur de calcul (Openfisca) pour améliorer la précision des simulations et la stabilité du service en production.

### Évolutions fonctionnelles
- Amélioration de l'identification des dispositifs spécifiques pour Paris Cité [#5160](https://github.com/betagouv/aides-jeunes/issues/5160).
- Correction de l'affichage des résultats pour les usagers déclarant un taux d'incapacité [#5212](https://github.com/betagouv/aides-jeunes/issues/5212).

### Évolutions techniques
- **Moteur Openfisca** :
  - Optimisation du calcul des coûts réels sur les tracés [#5211](https://github.com/betagouv/aides-jeunes/issues/5211).
  - Amélioration de la fiabilité des chemins d'erreur et limitation de la durée des calculs [#5205](https://github.com/betagouv/aides-jeunes/issues/5205).
  - Résolution d'incidents de production (erreurs 504) suite à une mise à jour du moteur [#5204](https://github.com/betagouv/aides-jeunes/issues/5204), [#5207](https://github.com/betagouv/aides-jeunes/issues/5207).
- **Sécurité & Infrastructure** :
  - Correction de l'authentification par jeton pour les appels échouant en iframe [#5210](https://github.com/betagouv/aides-jeunes/issues/5210).
- **Outils & Tests** :
  - Mise à jour des outils de test (Cypress) et de gestion des emails (Nodemailer, MJML) [#5148](https://github.com/betagouv/aides-jeunes/issues/5148), [#5146](https://github.com/betagouv/aides-jeunes/issues/5146).

### Autres changements
- **Maintenance de la veille** :
  - Nettoyage massif des aides dont les liens étaient cassés ou dont l'accès est devenu privé (notamment les aides au BAFA, les aides au permis de conduire, les prêts étudiants et divers dispositifs locaux).
  - Mise à jour des montants et conditions pour les stages à l'étranger [#5246](https://github.com/betagouv/aides-jeunes/issues/5246).
  - Correction des liens pour la bourse du secteur sanitaire et social en région Grand Est [#5173](https://github.com/betagouv/aides-jeunes/issues/5173).
