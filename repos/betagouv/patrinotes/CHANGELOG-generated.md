## Changelog : patrinotes (30 derniers jours)

### Résumé
Les dernières mises à jour de Patrinotes se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des alertes, de la génération de PDF et de l'interface mobile. De nombreuses corrections de bugs et améliorations de l'interface ont été apportées, ainsi que des optimisations techniques pour une meilleure performance et stabilité.

### Évolutions fonctionnelles
- Ajout de tests E2E pour améliorer la qualité de l'application. [#66](https://github.com/betagouv/patrinotes/issues/66)
- Amélioration de la gestion des alertes : possibilité de les désactiver complètement, de les gérer plus facilement et d'ajouter des emails associés.
- Amélioration de la génération de PDF : correction de problèmes d'affichage, ajout de contraintes pour le header, et amélioration de la gestion des liens.
- Amélioration de l'interface mobile : ajustements de la mise en page, des boutons et des champs de saisie pour une meilleure expérience sur les petits écrans.
- Ajout d'une section "Profil" dans les paramètres du compte.
- Ajout d'une fonctionnalité de recherche et d'autocomplétion pour les monuments historiques.
- Ajout d'une fonctionnalité de suppression avec confirmation pour les rapports et les états des rapports.
- Ajout d'un indicateur de synchronisation pour afficher l'état de la synchronisation des données.
- Ajout d'un bouton "Effacer" dans le formulaire de constat détaillé.
- Ajout de la possibilité de définir des services par défaut pour les alertes.
- Amélioration de la gestion des adresses dans les PDF (affichage complet).
- Amélioration de l'affichage des services et des comptes.

### Évolutions techniques
- Mise à jour de la bibliothèque Tanstack Query vers la version 5.
- Refactorisation de la gestion des alertes.
- Ajout de migrations pour la base de données.
- Amélioration de la gestion des erreurs et ajout de logs.
- Ajout d'une variable d'environnement pour activer/désactiver les alertes.
- Mise à jour de la configuration PWA.

### Autres changements
- Correction de nombreuses erreurs typographiques et améliorations de la lisibilité du code.
- Suppression de code obsolète.
- Amélioration de la documentation.
- Correction de problèmes liés à l'affichage des images.
- Suppression de l'occurrence de "crvif" dans le code.
- Remplacement de "null" par "" dans les PDF.
- Uniformisation du nom de l'application en "Patrinotes".
- Amélioration de la gestion des espaces blancs dans l'interface.
- Correction de bugs mineurs liés à la mise en page et au style.
