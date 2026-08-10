## Changelog : aides-jeunes (30 derniers jours, au 07/08/2026)

### Résumé
Ce mois-ci, l'activité s'est concentrée sur la fiabilité des informations proposées aux usagers et la stabilisation du moteur de calcul. Plusieurs liens vers des aides ont été corrigés ou mis à jour, et des améliorations techniques ont été apportées pour garantir la précision des résultats et la stabilité du service.

### Évolutions fonctionnelles
- **Maintenance des contenus** : Correction de liens cassés et mise à jour du statut (passage en privé) pour de nombreux dispositifs tels que le BAFA, le Pass Pass, les stages à l'étranger ou encore les fonds d'aide à la mobilité [#5165-5172, #5185-5190].
- **Correction de liens** : Mise à jour des liens concernant la Bourse du secteur sanitaire et social en région Grand Est [#5173].
- **Nouveauté locale** : Ajout d'un système permettant d'identifier spécifiquement les dispositifs pour Paris Centre [#5160].

### Évolutions techniques
- **Améliorations du moteur Openfisca** : Fiabilisation des calculs, gestion optimisée des erreurs, précision du budget pour les usagers déclarant un taux d'incapacité et amélioration du tracé des coûts réels [#5205, #5211, #5212].
- **Stabilité et production** : Résolution d'incidents de production (erreurs 504) liés aux mises à jour d'Openfisca [#5204, #5207].
- **Authentification** : Correction de l'authentification par jeton pour les appels échouant dans les iframes [#5210].
- **Maintenance des outils** : Mise à jour des outils de test et d'envoi d'emails (Cypress, Nodemailer, MJML) [#5146, #5148].
