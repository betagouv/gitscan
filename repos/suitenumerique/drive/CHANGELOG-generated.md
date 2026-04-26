## Changelog : drive (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur avec l'ajout d'un lecteur PDF intégré, des améliorations de l'interface pour la gestion des fichiers (duplication, colonnes personnalisables) et des corrections de bugs pour une meilleure stabilité. Des améliorations de sécurité et de performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un lecteur PDF intégré avec navigation par vignettes, zoom et navigation par pages. [#4567](https://github.com/suitenumerique/drive/issues/4567)
- Possibilité de dupliquer des fichiers et dossiers.
- Ajout de colonnes personnalisables dans l'explorateur de fichiers.
- Amélioration du menu d'actions sur mobile.
- Possibilité de configurer la durée de validité des invitations de partage.
- Amélioration des toasts d'upload avec indication de la progression, des erreurs et la possibilité d'annulation.
- Ajout d'une icône d'erreur réutilisable.
- Possibilité d'annuler les uploads en cours.
- Affichage de l'extension du fichier au lieu du type.

### Évolutions techniques
- Mise à jour de Django en version 5.2.13 (correction de sécurité).
- Mise à jour de pytest en version 9.0.3 (correction de sécurité).
- Mise à jour de Vite en version 6.4.2 (correction de sécurité).
- Mise à jour de Next.js en version 15.5.15 (correction de sécurité).
- Refonte de la gestion des previews de fichiers (optimisation et amélioration de la structure).
- Amélioration de la configuration du CI/CD (cache des navigateurs Playwright, pré-construction du frontend).
- Ajout d'une variable d'environnement pour la configuration de l'URL de l'email.
- Restriction du token du workflow drive-frontend pour une meilleure sécurité.
- Ajout d'une commande pour purger les éléments supprimés.
- Configuration d'une tâche cron quotidienne pour purger les éléments supprimés.
- Amélioration de la gestion des erreurs Pydantic pour une meilleure compatibilité avec le handler.
- Mise à jour de la librairie ds-proxy en version 2.0.0-alpha.4.

### Autres changements
- Mise à jour des traductions.
- Ajout de tests E2E pour les nouvelles fonctionnalités.
- Nettoyage du code et suppression de code inutilisé.
- Documentation mise à jour.
- Ajout de fichiers au .gitignore.
- Amélioration de la stabilité des tests E2E.
- Correction de problèmes de style et de mise en page.
- Ajout de commentaires et de documentation au code.
- Correction de problèmes de compatibilité avec différents navigateurs.
- Ajout de tests unitaires.
- Amélioration de la performance de certaines opérations.
