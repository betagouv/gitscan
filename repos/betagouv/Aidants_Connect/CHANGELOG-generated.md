## Changelog : Aidants_Connect (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment concernant la gestion des OTP (One-Time Password) pour la connexion, l'accès aux ressources et la gestion des formations. Des corrections de bugs et des ajustements ont également été effectués pour améliorer la stabilité et la clarté de l'application.

### Évolutions fonctionnelles
- Amélioration de l'intégration du formulaire de validation de l'OTP de la carte physique, incluant un format attendu et un message d'erreur plus clair. [#1723](https://github.com/betagouv/Aidants_Connect/issues/1723)
- Correction de l'affichage du QRCode dans l'interface d'administration pour l'association de moyens de connexion. [#1720](https://github.com/betagouv/Aidants_Connect/issues/1720)
- Restauration de la fonctionnalité de renouvellement de mandat. [#1717](https://github.com/betagouv/Aidants_Connect/issues/1717)
- Mise à jour du lien du tutoriel interactif dans la page Ressources. [#1721](https://github.com/betagouv/Aidants_Connect/issues/1721)
- Modification de l'intitulé de la catégorie "formation continue" en "formation". [#1716](https://github.com/betagouv/Aidants_Connect/issues/1716)
- Possibilité d'invalider la participation d'un apprenant à une formation. [#1714](https://github.com/betagouv/Aidants_Connect/issues/1714)
- Ajout de statistiques et d'améliorations à l'interface d'administration pour le PAP (Plan d'Action Personnalisé). [#1713](https://github.com/betagouv/Aidants_Connect/issues/1713)
- Ajout d'informations supplémentaires aux emails de statistiques. [#1705](https://github.com/betagouv/Aidants_Connect/issues/1705)
- Correction d'un bug dans l'API FNE (France Numérique Éducation). [#1715](https://github.com/betagouv/Aidants_Connect/issues/1715)

### Évolutions techniques
- Suppression de la dépendance `django-js-reverse`. [#1724](https://github.com/betagouv/Aidants_Connect/issues/1724)
- Mise à jour de Django de la version 4.2.27 à la version 4.2.28. [#1710](https://github.com/betagouv/Aidants_Connect/issues/1710)
- Refactoring des liens OTP dans l'administration pour utiliser l'espace de noms actuel du site d'administration.

### Autres changements
- Suppression d'une erreur Javascript sur la page d'accueil. [#1722](https://github.com/betagouv/Aidants_Connect/issues/1722)
- Suppression d'un bouton inutile lié à une lightbox vidéo.
- Correction d'un message d'erreur incorrect lors de la première connexion avec un moyen de connexion déjà configuré. [#1718](https://github.com/betagouv/Aidants_Connect/issues/1718)
- Amélioration de la validation du formulaire OTP pour restreindre l'entrée à 6 chiffres et améliorer le texte d'aide.
- Correction d'un bug lié à l'affichage des classes de formation à demi-journée.
- Correction d'un message de connexion incorrect.
- Suppression d'heures inutiles dans la représentation des formations.
