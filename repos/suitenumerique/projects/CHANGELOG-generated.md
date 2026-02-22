## Changelog : projects (30 derniers jours)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives de l'interface utilisateur, notamment sur les cartes et les listes Kanban. Des corrections de bugs ont été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant l'affichage des tableaux partagés et la gestion des utilisateurs. Des optimisations de performance ont également été réalisées, notamment en repensant la manière dont les utilisateurs sont chargés.

### Évolutions fonctionnelles
- Ajout d'un badge de nombre sur les en-têtes de liste pour indiquer le nombre de cartes. (#58)
- Attribution automatique des membres et des étiquettes filtrés aux cartes créées. (#57)
- Affichage par défaut de toutes les activités sur une carte, avec possibilité de les masquer. (#56)
- Amélioration de la recherche d'utilisateurs : les utilisateurs sont maintenant enregistrés localement lors de la recherche pour une meilleure performance et confidentialité. (#54)
- Masquage des adresses e-mail des utilisateurs lors de l'accès à un tableau public sans être connecté. (#54)
- Suppression de la fenêtre contextuelle de pièce jointe. (#53)

### Évolutions techniques
- Migration vers la version 2 du Kit UI. (#54)
- Remplacement de pnpm par npm pour simplifier la gestion des paquets et éviter les confusions.
- Alignement des versions de Node.js dans tous les environnements.
- Correction de problèmes liés à l'application des correctifs de paquets (`patch-package`) en environnement de développement.
- Suppression de la sauvegarde PostgreSQL Scalingo. (#53)

### Autres changements
- Correction de bugs d'interactions sur le modal des cartes. (#59)
- Correction de l'affichage des tableaux partagés dans le menu latéral. (#59)
- Mise à jour de la version de publication à 1.2.0. (#60)
- Mise à jour de la version de publication à 1.1.0. (#60)
