## Changelog : Aidants_Connect (30 derniers jours)

### Résumé
Au cours des dernières semaines, Aidants_Connect a bénéficié d'améliorations significatives, notamment concernant la gestion des formations, l'expérience utilisateur lors de la connexion et la gestion des mandats. Des corrections de bugs et des ajustements ont également été apportés pour améliorer la stabilité et la clarté de l'application.

### Évolutions fonctionnelles
- Possibilité d'invalider la participation d'un apprenant à une formation. [#1714](https://github.com/betagouv/Aidants_Connect/issues/1714)
- Le bouton de renouvellement de mandat est de nouveau visible sur la liste des mandats. [#1717](https://github.com/betagouv/Aidants_Connect/issues/1717)
- Amélioration de la validation du formulaire OTP (code à usage unique) pour restreindre l'entrée à 6 chiffres et améliorer l'aide contextuelle.
- Correction de l'affichage du QR code dans l'interface d'administration. [#1720](https://github.com/betagouv/Aidants_Connect/issues/1720)
- Mise à jour du lien vers le tutoriel interactif dans la page "Ressources". [#1721](https://github.com/betagouv/Aidants_Connect/issues/1721)
- Correction de l'API FNE (France Numérique Éducation). [#1715](https://github.com/betagouv/Aidants_Connect/issues/1715)
- Modification du libellé de la catégorie "formation continue" en "formation". [#1716](https://github.com/betagouv/Aidants_Connect/issues/1716)
- Amélioration des statistiques et de l'interface d'administration pour les PAP (Plans d'Accompagnement Personnalisés). [#1713](https://github.com/betagouv/Aidants_Connect/issues/1713)
- Ajout d'informations supplémentaires dans les emails de statistiques.
- Mise à jour du modèle d'email envoyé lors de la création d'un aidant. [#1705](https://github.com/betagouv/Aidants_Connect/issues/1705)

### Évolutions techniques
- Refactorisation des liens vers les dispositifs OTP dans l'administration pour utiliser l'espace de noms actuel et ajouter l'affichage du lien QR code.
- Ajout du format attendu pour l'association d'un moyen de connexion. [#1719](https://github.com/betagouv/Aidants_Connect/issues/1719)
- Correction des tests de connexion incorrecte.
- Modification du message d'erreur de connexion incorrect.
- Amélioration de l'affichage des formations (suppression des heures et des formations à demi-journée).

### Autres changements
- Mise à jour de la dépendance Django de la version 4.2.27 à la version 4.2.28. [#1710](https://github.com/betagouv/Aidants_Connect/issues/1710)
- Correction de petites erreurs de typographie.
