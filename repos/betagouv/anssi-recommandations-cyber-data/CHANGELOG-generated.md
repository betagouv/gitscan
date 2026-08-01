## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 27 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment pour la gestion des collections Albert et des documents. Des corrections de sécurité ont également été apportées, ainsi que des optimisations pour la gestion des identifiants et la configuration du projet.

### Évolutions fonctionnelles
- Ajout de la possibilité de supprimer des documents. [#72ae2e6](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/72ae2e6)
- Ajout d'un sélecteur de collection pour faciliter le choix de la collection Albert à utiliser. [#817e34e](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/817e34e)
- Affichage de l'identifiant de la collection dans la liste déroulante pour distinguer les collections. [#cb3f42d](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/cb3f42d)
- Possibilité d'ajouter un document HTML depuis une URL. [#e47f117](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/e47f117)
- Ajout d'un formulaire pour "jeopardiser" (supprimer l'index) une collection entière. [#b14126a](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/b14126a)
- Redirection vers le TDB après authentification. [#f2ab570](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/f2ab570)
- Correction : Lors de la suppression d'un document MSC, le document "miroir" dans la collection Jeopardy est maintenant également supprimé. [#fea161f](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/fea161f)
- Correction : Le tableau de documents interroge maintenant la collection sélectionnée et non plus les collections par défaut. [#1e50ca6](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/1e50ca6)
- Correction : L'enrôlement fonctionne correctement avec le bon nom d'utilisateur. [#0f94d12](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/0f94d12)
- Correction : Les noms de documents sont maintenant encodés en UTF-8. [#cece025](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/cece025)

### Évolutions techniques
- Mise à jour de la dépendance Docling vers une version >= 2.97.0 pour des raisons de sécurité. [#a8d9e8e](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/a8d9e8e)
- Ajout d'outils de sécurité : `zizmor` pour la validation de la configuration. [#685a93e](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/685a93e)
- Désactivation des identifiants `git` des dépôts clonés pour renforcer la sécurité. [#94041bd](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/94041bd)
- Refactorisation : Extraction d'un composant `PageInformationsCollections`. [#acf723a](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/acf723a)
- Ajout d'une route GET `/collections/disponibles` pour récupérer les collections Albert. [#4217447](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/4217447)

### Autres changements
- Ajout de l'action Renovate pour la gestion automatisée des dépendances. [#19f167b](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/19f167b)
- Mises à jour automatiques de plusieurs dépendances (tailwindcss, @lab-anssi/ui-kit, postcss, vite, autoprefixer, prettier, eslint-plugin-svelte, sass-embedded, svelte, globals) via Renovate.
