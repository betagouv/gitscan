## Changelog : mobilic (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface d'administration, notamment avec l'ajout d'une page d'accueil centralisée et la refonte de la gestion des véhicules. Des améliorations ont également été apportées à la gestion des activités et à la sécurité, avec l'implémentation de l'authentification à deux facteurs (TOTP) et de la possibilité d'usurper l'identité d'un utilisateur pour l'assistance. Enfin, un widget de chat en direct a été intégré pour améliorer le support utilisateur.

### Évolutions fonctionnelles
- Ajout d'une page d'accueil pour les administrateurs avec un tableau de bord et un aperçu des infractions. [#826](https://github.com/MTES-MCT/mobilic/pulls/826)
- Refonte de la gestion des véhicules avec une nouvelle modale d'importation en masse et la possibilité d'ajouter des véhicules directement depuis la liste. [#837](https://github.com/MTES-MCT/mobilic/pulls/837), [#849](https://github.com/MTES-MCT/mobilic/pulls/849)
- Implémentation de l'authentification à deux facteurs (TOTP) pour une sécurité renforcée. [#840](https://github.com/MTES-MCT/mobilic/pulls/840)
- Ajout de la fonctionnalité d'usurpation d'identité d'utilisateur pour l'assistance. [#841](https://github.com/MTES-MCT/mobilic/pulls/841)
- Intégration d'un widget de chat en direct Brevo pour le support utilisateur. [#832](https://github.com/MTES-MCT/mobilic/pulls/832)
- Ajout d'étiquettes d'état pour les missions dans l'onglet "Activités". [#835](https://github.com/MTES-MCT/mobilic/pulls/835)
- Possibilité de rechercher des articles natinf dans le contrôle. [#842](https://github.com/MTES-MCT/mobilic/pulls/842)
- Amélioration de l'affichage des activités passées (missions en dehors de la fenêtre de 31 jours). [#839](https://github.com/MTES-MCT/mobilic/pulls/839)

### Évolutions techniques
- Refactorisation du code pour améliorer la performance et la maintenabilité.
- Utilisation d'icônes DSFR dans les actions d'édition de tableau. [#836](https://github.com/MTES-MCT/mobilic/pulls/836)
- Amélioration de la validation des numéros d'immatriculation des véhicules. [#845](https://github.com/MTES-MCT/mobilic/pulls/845)
- Optimisation du cache des données du tableau de bord. [#848](https://github.com/MTES-MCT/mobilic/pulls/848)
- Extraction de constantes et de logique réutilisable pour améliorer la cohérence du code.
- Mise à jour de la politique de confidentialité et des informations relatives au traitement des données Brevo. [#832](https://github.com/MTES-MCT/mobilic/pulls/832)

### Autres changements
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Mise à jour de la documentation.
- Correction de problèmes de duplication de code détectés par SonarCloud.
- Amélioration de l'accessibilité du widget de chat en direct.
- Ajout du logo Mobilic sur le bouton du chat en direct Brevo.
