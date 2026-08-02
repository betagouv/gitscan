## Changelog : ComparIA (30 derniers jours, au 17 juillet 2026)

### Résumé
Les récentes évolutions de ComparIA se concentrent sur l'amélioration de la stabilité et de la maintenabilité de la plateforme, avec l'ajout d'un mode maintenance pour faciliter les opérations. L'interface utilisateur a également été améliorée, notamment avec la correction du lien vers les datasets Hugging Face et une refonte de la page d'accueil pour encourager le déploiement auto-hébergé.

### Évolutions fonctionnelles
- Ajout d'un mode maintenance pour permettre des opérations de maintenance sans affecter les utilisateurs. Le mode maintenance redirige automatiquement vers la page d'accueil. [#570](https://github.com/betagouv/ComparIA/pull/570)
- Correction du lien vers les datasets Hugging Face sur la page Datasets. [#575](https://github.com/betagouv/ComparIA/pull/575)
- Refonte de la page d'accueil (README) pour mettre l'accent sur le déploiement auto-hébergé. [#578](https://github.com/betagouv/ComparIA/pull/578)
- Ajout de commandes `comperia-cli` pour la sauvegarde de la base de données et la déconnexion des connexions DB pendant la maintenance. [#569](https://github.com/betagouv/ComparIA/pull/569) et [#570](https://github.com/betagouv/ComparIA/pull/570)

### Évolutions techniques
- Refactorisation du message système (system message) pour améliorer la clarté et la maintenabilité. [#555](https://github.com/betagouv/ComparIA/pull/555)
- Correction de la gestion des LLMs inconnus pour éviter les erreurs. [#556](https://github.com/betagouv/ComparIA/pull/556)
- Diminution du taux d'échantillonnage Sentry par défaut pour réduire le volume de traces et améliorer les performances. [#588](https://github.com/betagouv/ComparIA/pull/588)
- Suppression d'un helper inutilisé `set_maintenance_mode`. [#572](https://github.com/betagouv/ComparIA/pull/572)

### Autres changements
- Mise à jour des traductions pour le norvégien Bokmål, l'espagnol et l'anglais via Weblate.
- Mise à jour des traductions pour l'italien via Weblate.
- Intégration des dernières mises à jour de Weblate.
- Augmentation des limites de débit par IP pour la sélection personnalisée (temporaire). [#554](https://github.com/betagouv/ComparIA/pull/554)
