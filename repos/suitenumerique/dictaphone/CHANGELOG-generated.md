## Changelog : dictaphone (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur le développement d'une application mobile (iOS et Android) pour Dictaphone, l'amélioration de l'intégration avec des services externes comme Docs, et l'ajout de fonctionnalités de gestion des enregistrements, notamment la corbeille et la suppression définitive. Des améliorations significatives ont également été apportées à l'interface utilisateur web et mobile, ainsi qu'à la robustesse et la sécurité du backend.

### Évolutions fonctionnelles
- Ajout d'une application mobile (iOS et Android) avec les fonctionnalités de base : enregistrement, liste des enregistrements, lecture, suppression et connexion utilisateur.
- Intégration avec Docs pour la transcription et l'accès aux transcriptions.
- Implémentation d'une corbeille pour les enregistrements supprimés, permettant leur restauration.
- Possibilité de supprimer définitivement les enregistrements de la corbeille.
- Ajout d'un lien "Ouvrir dans Docs" pour faciliter l'accès aux transcriptions.
- Amélioration de la gestion des erreurs et des retours d'information à l'utilisateur (ex: retry upload).
- Ajout d'un lien vers la documentation dans l'application mobile.
- Possibilité de télécharger l'application mobile depuis le menu d'aide sur le web.
- Ajout d'un indicateur de progression pendant le téléchargement des fichiers.
- Amélioration de la gestion des autorisations sur Android.
- Ajout d'une option pour supprimer un compte utilisateur depuis l'application mobile.

### Évolutions techniques
- Refonte de l'authentification mobile avec JWT et PKCE pour une meilleure sécurité.
- Mise à jour des dépendances backend et Dockerfiles.
- Amélioration des tests backend et généralisation des tests.
- Suppression de vérifications inutiles dans le CI.
- Amélioration de la journalisation (logging) pour faciliter le débogage.
- Support amélioré des formats audio m4a.
- Mise en place d'un système d'analyse (PostHog) pour suivre l'utilisation de l'application.
- Amélioration de la gestion des erreurs lors de l'appel à l'API Docs.
- Mise en place d'un système de gestion des versions pour l'application mobile.
- Amélioration de la gestion des configurations pour l'application mobile.
- Utilisation de React Native Nitro Player pour la lecture audio sur mobile.

### Autres changements
- Mise à jour de la documentation.
- Amélioration de la structure du code et nettoyage.
- Corrections de bugs mineurs dans l'interface utilisateur web et mobile.
- Mise à jour des logos et des icônes.
- Amélioration de la traduction en français.
- Correction de problèmes de typographie et de formatage.
- Suppression de l'écriture inclusive dans la documentation.
- Amélioration des styles et des couleurs de l'interface utilisateur.
- Mise à jour des dépendances React Native pour l'application mobile.
