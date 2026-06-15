## Changelog : meet (30 derniers jours, au 2026-06-14)

### Résumé
Ce mois-ci, l'équipe a apporté des améliorations significatives à la plateforme Meet, axées sur l'expérience utilisateur, la sécurité et la flexibilité. Les nouveautés incluent des options de configuration avancées pour les salles de réunion, des améliorations de la qualité audio, des correctifs de sécurité et des optimisations des performances, notamment grâce au chargement différé de certains composants. L'addon Outlook a également été enrichi de nouvelles fonctionnalités.

### Évolutions fonctionnelles
- Possibilité de masquer le bouton de connexion via un paramètre d'URL.
- Possibilité de désactiver la connexion silencieuse via un paramètre d'URL.
- Amélioration de la réduction du bruit avec un pipeline de traitement audio BBBA.
- Ajout d'un menu d'options dans la fenêtre "image dans l'image" (PiP) pour un contrôle plus facile.
- Prise en charge de la désactivation du micro des participants par les administrateurs de la salle, configurable au niveau de la salle.
- Ajout d'un lien vers un formulaire de feedback dans le pied de page de l'addon Outlook.
- Amélioration de l'addon Outlook : support de l'internationalisation, lien de feedback, et amélioration de la génération de liens.
- Support étendu pour tous les types de fichiers audio/vidéo.
- Ajout d'un administrateur spécifique aux fichiers.

### Évolutions techniques
- Optimisation des performances du frontend grâce au chargement différé de `@libreaudio/la-call` et d'autres composants.
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (react-i18next, urllib3, idna, core-js, webpack-dev-server).
- Refactorisation du code frontend pour améliorer la modularité et le code splitting.
- Amélioration de la synchronisation de la configuration des salles de réunion entre le backend et le frontend.
- Utilisation d'imports SVG individuels pour les icônes Material afin d'optimiser la taille des ressources.
- Refactorisation de la gestion des permissions de mise en sourdine.
- Amélioration de la robustesse du processus de suppression de fichiers sur le backend.
- Mise à jour des versions des charts Helm.
- Ajout d'une commande de gestion pour fusionner les utilisateurs en double.
- Amélioration de la gestion des erreurs et des conditions de concurrence lors de la création d'utilisateurs.
- Remplacement de l'API Room Options dépréciée.
- Mise à jour de ESLint vers la version 9.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités de l'API.
- Correction de bugs mineurs liés à la position des tooltips et au recentrage de la barre de réactions.
- Amélioration de la configuration des variables d'environnement pour le backend et le développement.
- Ajout d'un visualiseur de bundle Rollup pour faciliter le débogage des performances du frontend.
- Correction de problèmes de compatibilité avec ProConnect.
- Correction d'un bug d'audio mono dans la réduction du bruit.
- Correction d'un bug empêchant la fermeture automatique des dialogues dans l'addon Outlook.
- Correction d'un bug lié à l'absence de `default-src` dans la configuration CSP.
- Correction d'un bug lié à l'affichage du message de fallback lorsque le dialogue ne peut pas se fermer automatiquement.
- Correction d'un bug empêchant l'insertion du lien de réunion à la position du curseur dans l'addon Outlook.
- Correction d'un bug lié à l'affichage du tag "beta" dans l'addon Outlook.
- Correction d'un bug lié à la génération de liens lorsque l'événement en contient déjà un.
- Correction d'un bug lié au changement de bouton "ajouter" en "supprimer" lorsque le lien existe déjà.
- Correction d'un bug lié à la gestion des erreurs lors de la suppression de fichiers.
- Mise à jour du changelog.
