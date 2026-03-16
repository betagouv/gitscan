## Changelog : Aidants_Connect (30 derniers jours)

### Résumé
Au cours des dernières semaines, Aidants_Connect a bénéficié d'améliorations significatives pour les conseillers numériques, notamment en ce qui concerne la gestion des parcours de formation et des mandats. Des corrections de bugs et des améliorations de l'interface ont également été apportées pour améliorer l'expérience utilisateur, en particulier concernant la validation OTP et l'affichage des informations. Des suppressions de fonctionnalités obsolètes ont également été effectuées pour simplifier l'application.

### Évolutions fonctionnelles
- Possibilité de basculer un aidant d'un parcours classique vers un parcours "papier" via l'interface d'administration. [#1730](https://github.com/betagouv/Aidants_Connect/issues/1730)
- Action pour l'inscription et le basculement de session pour les conseillers numériques, avec modélisation du financement. [#1727](https://github.com/betagouv/Aidants_Connect/issues/1727)
- Amélioration de l'intégration du formulaire de validation du code OTP (One-Time Password) pour la carte physique, avec un format attendu plus clair. [#1723](https://github.com/betagouv/Aidants_Connect/issues/1723)
- Correction de l'affichage du QR code dans l'interface d'administration pour l'association d'un moyen de connexion. [#1720](https://github.com/betagouv/Aidants_Connect/issues/1720)
- Possibilité d'invalider la participation d'un apprenant à une formation. [#1714](https://github.com/betagouv/Aidants_Connect/issues/1714)
- Ajout de la possibilité de renouveler un mandat. [#1717](https://github.com/betagouv/Aidants_Connect/issues/1717)
- Mise à jour de l'email envoyé lors de la création d'un aidant. [#1705](https://github.com/betagouv/Aidants_Connect/issues/1705)
- Amélioration de l'interface pour la gestion des formations, notamment l'affichage des plannings et la suppression des demi-journées. [#1713](https://github.com/betagouv/Aidants_Connect/issues/1713)
- Modification du message d'erreur lors d'une tentative de connexion incorrecte. [#1716](https://github.com/betagouv/Aidants_Connect/issues/1716)

### Évolutions techniques
- Mise à jour de Django de la version 4.2.28 à la version 4.2.29. [#1726](https://github.com/betagouv/Aidants_Connect/issues/1726) et [#1710](https://github.com/betagouv/Aidants_Connect/issues/1710)
- Suppression de la dépendance `django-js-reverse`. [#1724](https://github.com/betagouv/Aidants_Connect/issues/1724)
- Suppression des vues liées à Datapass. [#1728](https://github.com/betagouv/Aidants_Connect/issues/1728) et [#1725](https://github.com/betagouv/Aidants_Connect/issues/1725)
- Refactorisation des liens vers les dispositifs OTP dans l'administration pour utiliser l'espace de noms actuel.
- Correction de tests suite à des modifications.

### Autres changements
- Ajout de tests d'accessibilité sur les pages publiques. [#1729](https://github.com/betagouv/Aidants_Connect/issues/1729)
- Correction de fautes de frappe et amélioration de l'accessibilité dans les templates.
- Mise à jour du lien du tutoriel interactif dans la page Ressources. [#1721](https://github.com/betagouv/Aidants_Connect/issues/1721)
- Suppression d'une lightbox vidéo inutile sur la page d'accueil. [#1722](https://github.com/betagouv/Aidants_Connect/issues/1722)
- Renommage de la catégorie "formation continue" en "formation". [#1716](https://github.com/betagouv/Aidants_Connect/issues/1716)
- Ajout d'informations supplémentaires dans les emails de statistiques.
- Amélioration de l'interface d'administration pour les parcours "papier" et les statistiques.
