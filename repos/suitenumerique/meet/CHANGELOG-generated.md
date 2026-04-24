## Changelog : meet (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la sécurité, de l'accessibilité et de la robustesse de la plateforme Meet. Des corrections de vulnérabilités ont été apportées, l'accessibilité a été renforcée pour les utilisateurs ayant des besoins spécifiques, et des améliorations ont été faites à la collecte de métadonnées pour mieux comprendre l'utilisation de la plateforme. De nouvelles fonctionnalités sont également en préparation, notamment l'amélioration de la transcription et du résumé des réunions.

### Évolutions fonctionnelles
- Ajout de la prise en charge de formats de fichiers supplémentaires pour le partage de documents [#1265].
- Amélioration de la gestion des tâches de transcription et de résumé, avec une API plus proche des exigences du gateway [#1171].
- Possibilité de télécharger les enregistrements avec un titre de document explicite pour une meilleure accessibilité [#1261].
- Amélioration du raccourci clavier pour la barre de réactions, permettant de la rouvrir facilement [#1262].

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (Pillow, aiohttp, vite, django, pytest).
- Refactorisation du système de réactions pour unifier l'état et le rendu, améliorant ainsi la maintenabilité du code.
- Utilisation de l'en-tête `Authorization` pour l'authentification des tokens LiveKit, renforçant la sécurité.
- Amélioration de la gestion des erreurs Twirp pour les opérations sur les participants.
- Ajout de la collecte de métadonnées sur les événements VAD (Voice Activity Detection), de connexion et de chat pour une meilleure analyse de l'utilisation.
- Mise à jour de l'image frontend pour utiliser Alpine 3.23, corrigeant ainsi des vulnérabilités.
- Pinning de l'image Docker pour des builds reproductibles.
- Amélioration des tests unitaires pour le service de gestion des tokens JWT.
- Ajout de la prise en charge de l'authentification multi-tenant.

### Autres changements
- Amélioration de la documentation pour la méthode de résumé.
- Suppression d'outils de développement obsolètes pour Tilt.
- Corrections de l'indentation dans le Makefile.
- Ajout de variables d'environnement pour les secrets dans Tilt.
- Amélioration des logs pour ne plus inclure d'adresses email sensibles.
- Ajout de contextes de sécurité pour les pods et conteneurs dans Helm.
- Suppression de valeurs Helm inutilisées.
- Optimisation de l'utilisation des sondages PostHog et enrichissement des métadonnées des événements.
- Suppression de la commande de récupération des secrets externes obsolète.
- Initialisation des secrets Kubernetes pour l'environnement de développement Tilt.
- Correction de la simulation d'erreurs Twirp dans les tests.
- Ajout de support pour Compose pour le service multi-user-transcriber.
- Amélioration de la gestion des erreurs dans le webhook de notification.
- Ajout d'un ignore ruff pour la commande ffprobe.
- Correction du format de payload whisperX.
- Ajout de support pour le format webm.
