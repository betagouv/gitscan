## Changelog : fonds-prevention-argile (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives pour les agents de l'administration, notamment l'ajout de la gestion des dossiers par type d'accompagnement (AV, AMO, AV+AMO) et l'ajout d'un iframe pour les partenaires. Des corrections ont également été apportées pour améliorer la stabilité et la sécurité de l'application, ainsi que des améliorations de l'expérience utilisateur, comme le préremplissage du numéro de téléphone et l'ajout d'une source d'acquisition lors de l'inscription.

### Évolutions fonctionnelles
- Les agents peuvent désormais ajouter des dossiers en spécifiant le type d'accompagnement : AV, AMO ou AV + AMO.  [#195](https://github.com/MTES-MCT/fonds-prevention-argile/issues/195)
- Ajout d'un champ "autre raison" manquant dans un formulaire. [#196](https://github.com/MTES-MCT/fonds-prevention-argile/issues/196)
- Intégration d'un iframe pour afficher le contenu des partenaires. [#192](https://github.com/MTES-MCT/fonds-prevention-argile/issues/192)
- Mise à jour du lien vers l'arrêté. [#193](https://github.com/MTES-MCT/fonds-prevention-argile/issues/193)
- Ajout du préremplissage du numéro de téléphone pour faciliter la saisie. [#190](https://github.com/MTES-MCT/fonds-prevention-argile/issues/190)
- Ajout de la source d'acquisition dans le modal d'inscription pour un meilleur suivi. [#183](https://github.com/MTES-MCT/fonds-prevention-argile/issues/183)
- Ajout d'un graphique pour visualiser l'évolution du nombre d'utilisateurs. [#184](https://github.com/MTES-MCT/fonds-prevention-argile/issues/184)
- Intégration d'un nouvel arrêté. [#170](https://github.com/MTES-MCT/fonds-prevention-argile/issues/170) et [#179](https://github.com/MTES-MCT/fonds-prevention-argile/issues/179)

### Évolutions techniques
- Mise en place d'un CRON pour la synchronisation et nettoyage de la démarche de diagnostic. [#189](https://github.com/MTES-MCT/fonds-prevention-argile/issues/189)
- Implémentation de `verifyProspectTerritoryAccess` et correction d'une vulnérabilité IDOR (Insecure Direct Object Reference). [#186](https://github.com/MTES-MCT/fonds-prevention-argile/issues/186)
- Correction d'un problème lié à l'endpoint `run after`. [#191](https://github.com/MTES-MCT/fonds-prevention-argile/issues/191)
- Corrections de bugs divers (w). [#187](https://github.com/MTES-MCT/fonds-prevention-argile/issues/187) et [#188](https://github.com/MTES-MCT/fonds-prevention-argile/issues/188)

### Autres changements
- Correction du contenu JSON de la page d'accueil. [#185](https://github.com/MTES-MCT/fonds-prevention-argile/issues/185)
