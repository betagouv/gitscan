## Changelog : patrinotes (30 derniers jours)

### Résumé
Les dernières mises à jour de Patrinotes se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des constats détaillés et des rapports d'état. De nombreuses corrections de bugs ont été apportées pour améliorer la stabilité et la fiabilité de l'application, en particulier concernant la génération de PDF et la gestion des formulaires. Des améliorations ont également été apportées à la navigation et à l'interface utilisateur.

### Évolutions fonctionnelles
- Ajout de tests E2E pour améliorer la couverture des tests et la qualité de l'application. [#66](https://github.com/betagouv/patrinotes/issues/66)
- Amélioration des fonctionnalités de constat détaillé et de gestion des comptes, avec ajout de tests associés. [#67](https://github.com/betagouv/patrinotes/issues/67)
- Possibilité de masquer complètement le bouton d'alertes.
- Ajout d'une fonctionnalité pour personnaliser l'en-tête des PDF pour qu'il s'adapte à n'importe quel service.
- Ajout d'une nouvelle navigation dans les pages de rapport d'état, avec une barre de navigation collante.
- Ajout de la possibilité de créer des monuments historiques personnalisés.
- Ajout d'un bouton "Effacer" dans le constat détaillé pour faciliter la saisie des informations.
- Ajout d'une confirmation modale lors de la suppression d'un rapport ou d'un rapport d'état.
- Ajout d'une option pour activer/désactiver la fonctionnalité d'alertes via une variable d'environnement.
- Amélioration de l'affichage de l'adresse complète dans les PDF.
- Correction de l'affichage des boutons "MH non lié" et des alertes sur mobile.
- Correction de l'entrée d'email CRVIF.
- Correction de l'ordre des services affichés.
- Correction du bug empêchant la sauvegarde correcte du titre du rapport d'état non lié.
- Correction de l'affichage des tags d'email.
- Correction du bug de duplication des rapports d'état.

### Évolutions techniques
- Suppression de toutes les occurrences de "crvif" dans le code.
- Remplacement de "null" par une chaîne vide dans la génération de PDF.
- Mise à jour de la configuration PWA pour refléter le nouveau nom de l'application ("Patrinotes").
- Remplacement de "patrinotes" dans tout le code pour assurer la cohérence.
- Ajout de logs d'erreur pour faciliter le débogage.
- Ajout d'une variable d'environnement pour l'hôte autorisé.
- Mise à jour de la CI.

### Autres changements
- Mise à jour du fichier README.md.
- Correction de fautes de frappe dans le code et la documentation.
- Correction de problèmes de marges dans la page service/compte.
- Correction d'un bug d'affichage du message d'erreur de connexion.
- Correction de l'utilisation de "isSectionVisited" dans le formulaire et le PDF.
- Suppression d'une ancienne variable d'environnement.
- Correction du titre et de l'image dans l'en-tête PDF pour éviter les coupures.
- Correction du flicker du destinataire.
- Correction du texte Marianne dans l'en-tête PDF.
- Ajout de contraintes pour l'en-tête PDF.
- Correction de la suppression d'image dans CRVIF.
- Correction de la confirmation modale sur mobile.
- Correction de la suppression de clause.
- Mise en minuscule des emails suggérés.
- Correction du bug de duplication du rapport d'état.
- Correction du bug empêchant le formulaire d'informations de se vider lors de la modification du titre du rapport d'état.
- Correction des sections speechtotext du constat détaillé.
- Correction du message d'erreur de connexion.
