## Changelog : tchap-x-android (30 derniers jours, au 18 juillet 2026)

### Résumé
Cette mise à jour apporte des corrections de compatibilité pour les appareils 32 bits, des améliorations de la connexion avec Tchap Classique, et des ajustements pour l'activation des salons privés non-chiffrés. Plusieurs versions intermédiaires ont été publiées pour stabiliser l'application et corriger des problèmes spécifiques. L'application a également été renommée en "Tchap" pour la version beta.

### Évolutions fonctionnelles
- Correction d'un problème de compatibilité pour les appareils 32 bits [#916280a72c, #13e9519074].
- Amélioration de la connexion via Tchap Classique avec ProConnect [#7bd7a33f01].
- Activation des salons privés non-chiffrés [#6b812802f0].
- Ajout d'un badge "Recommandé" pour les salons privés chiffrés [#519ed37fd8].
- Ajout de la commande `/visio` pour lancer un appel vidéo [#132aeafe86].
- Activation des commandes dans les messages [#2157fcc8b4].
- Mise à jour des certificats de juillet 2026 [#7518e72b7f].
- Renommage de l'application Tchap beta en Tchap [#a3fea70d86].
- Ajout d'instructions pour activer la sauvegarde automatique dans Tchap Classique [#4712546b22].
- Affichage d'un texte d'alerte lors du partage d'un fichier dans un salon non chiffré [#48e7c8410e].
- Suppression de l'affichage du bandeau de réinitialisation d'identité d'un membre [#61ecf4c478].

### Évolutions techniques
- Changement du format de numéro de version [#72f5f3555f].
- Suppression des noms de domaine Element non utilisés [#a5bcfa26b4].
- Mise à jour de Compound et amélioration des badges [#624e73bb76].
- Configuration des URL de Push en fonction de l'environnement [#0b8d1a6dbe].
- Suppression de la bordure pour les badges neutres [#31839dba2d].
- Remplacement du logo Tchap sur Android Studio [#f15bcee146].
- Réduction de la taille des logs pour éviter les erreurs serveur [#873a43a968].
- Désactivation temporaire de Unified Push en raison de problèmes de fonctionnement [#35e1699a51].

### Autres changements
- Mise à jour du lien du Play Store dans le script de release [#f17037e507].
- Rendu monochrome du logo Tchap dans le centre de notification [#33a4c997bb].
- Plusieurs releases intermédiaires (26.07.0, 26.07.1, 26.07.2, 26.07.3, 26.07.4, 26.07.5, 26.07.6) pour corrections et stabilisations.
