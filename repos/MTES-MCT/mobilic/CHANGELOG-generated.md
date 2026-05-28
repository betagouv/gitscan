## Changelog : mobilic (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface d'administration, notamment la page d'accueil et la gestion des véhicules. Des corrections ont été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant la validation des missions, l'importation en masse de véhicules et la gestion des infractions. L'authentification a été renforcée avec l'ajout de l'authentification à deux facteurs (2FA) et la possibilité d'usurpation d'identité pour le support.

### Évolutions fonctionnelles
- Ajout d'un logo pour Chaventon Express [#848](https://github.com/MTES-MCT/mobilic/pulls/848).
- Amélioration de la page d'accueil de l'administration avec affichage des jours multi-employeurs et distinction entre semaines complètes et incomplètes [#851](https://github.com/MTES-MCT/mobilic/pulls/851), [#854](https://github.com/MTES-MCT/mobilic/pulls/854).
- Refonte de l'importation en masse de véhicules avec prise en compte des retours de recette [#837](https://github.com/MTES-MCT/mobilic/pulls/837), [#845](https://github.com/MTES-MCT/mobilic/pulls/845).
- Ajout de la recherche NATINF dans l'interface de contrôle [#842](https://github.com/MTES-MCT/mobilic/pulls/842).
- Implémentation de l'authentification à deux facteurs (2FA) avec code TOTP [#826](https://github.com/MTES-MCT/mobilic/pulls/826).
- Ajout de la fonctionnalité d'usurpation d'identité pour le support administratif, incluant une interface de recherche et un affichage clair de l'utilisateur usurpé.
- Amélioration de l'affichage des activités et correction du calendrier de sélection de date.
- Correction de l'affichage des missions datant de plus de 31 jours.

### Évolutions techniques
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment dans les composants liés à la gestion des dates et des activités.
- Utilisation de constantes pour les couleurs et les formats de date afin d'assurer une cohérence visuelle.
- Utilisation d'icônes DSFR dans l'interface d'administration.
- Optimisation de la validation des numéros d'immatriculation des véhicules.
- Suppression de code inutilisé et correction de problèmes de duplication de code détectés par SonarCloud.
- Amélioration de la gestion des erreurs et des retours d'API.

### Autres changements
- Mise à jour de la documentation et des textes de l'interface de sécurité.
- Correction de typos et amélioration de la qualité du code.
- Ajout de tests pour certaines fonctionnalités.
- Mise à jour des dépendances.
- Amélioration du suivi des assets DSFR.
