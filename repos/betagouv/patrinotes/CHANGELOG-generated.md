## Changelog : patrinotes (30 derniers jours, au 10 mars 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la génération de rapports PDF, la correction de bugs et l'amélioration de l'expérience utilisateur, notamment dans la gestion des rapports d'état et des services. Des tests E2E ont également été ajoutés pour renforcer la qualité du logiciel.

### Évolutions fonctionnelles
- Amélioration du détail des constats et des fonctionnalités liées aux comptes, avec ajout de tests associés. [#67](https://github.com/betagouv/patrinotes/issues/67)
- Ajout de tests E2E (end-to-end) pour une meilleure couverture des tests fonctionnels. [#66](https://github.com/betagouv/patrinotes/issues/66)
- Possibilité de masquer complètement le bouton d'alertes sur certaines pages.
- Désactivation des alertes au niveau de la page service.
- Amélioration de l'affichage des boutons "MH" (Marianne) sur mobile.
- Affichage de l'adresse complète dans les rapports PDF.
- Transformation du texte de l'en-tête PDF pour s'adapter à n'importe quel service.
- Ajout de contraintes pour l'en-tête PDF.
- Ajout de la possibilité de créer des MH (Marianne) personnalisés.
- Ajout d'une nouvelle navigation dans les pages de rapport d'état, avec une barre de navigation "sticky".
- Correction de l'affichage du titre du rapport d'état lors de la sauvegarde.
- Correction de l'ordre des services lors de l'affichage.
- Correction de l'affichage des sections speechtotext dans le constat détaillé.
- Correction de l'utilisation de "isSectionVisited" sur le formulaire et le PDF.
- Correction du message d'erreur de connexion.
- Correction de la marge service/compte.
- Correction de l'affichage de l'image sur CRVIF.
- Correction de la modale de confirmation sur mobile.
- Correction du flickering du destinataire.
- Correction du texte Marianne dans l'en-tête PDF.
- Correction de la redirection si le rapport d'état est vide.
- Correction de la modale de suppression de rapport.
- Correction de la duplication de rapport d'état.
- Suppression de l'ancienne variable d'environnement.

### Évolutions techniques
- Suppression de toutes les occurrences de "crvif" dans le code.
- Remplacement de "null" par "" dans les rapports PDF.
- Mise à jour de la configuration PWA (Progressive Web App) pour refléter le nouveau nom de l'application.
- Remplacement de toutes les références à l'ancien nom de l'application par "Patrinotes".
- Ajout de logs d'erreur pour faciliter le débogage.
- Ajout de la variable d'environnement `ALLOWED_HOST`.
- Mise à jour de la CI (Continuous Integration).

### Autres changements
- Mise à jour du fichier README.md.
- Correction d'une faute de frappe dans le PDF.
- Correction de la casse des suggestions d'emails.
- Suppression de clause de suppression.
- Correction de la suppression d'image sur CRVIF.
- Correction du bug empêchant le formulaire d'informations de se vider lors de la modification du titre du rapport d'état.
- Correction d'un bug lié à la sauvegarde de l'état "non lié".
