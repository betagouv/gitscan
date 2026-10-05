## Changelog : grist-plugin-opendata (30 derniers jours, au 02/10/2026)

### Résumé
Cette période a été consacrée à une modernisation profonde de l'infrastructure du plugin. L'adoption de nouveaux outils de build et de gestion de paquets, ainsi que l'ajout du support Docker, visent à rendre le projet plus performant et plus facile à déployer. Une correction a également été apportée pour améliorer la clarté des messages de validation des données.

### Évolutions fonctionnelles
- Correction de l'affichage de la bannière de schéma : celle-ci ne s'affiche désormais qu'en cas de succès de la validation, évitant toute confusion pour l'utilisateur.

### Évolutions techniques
- **Modernisation du build et de la gestion de paquets** :
    - Migration complète vers Vite pour accélérer les processus de build.
    - Passage à `pnpm` comme gestionnaire de paquets [#46](https://github.com/datagouv/grist-plugin-opendata/pull/46).
- **Amélioration du déploiement** :
    - Ajout d'un Dockerfile utilisant Nginx pour faciliter la conteneurisation du plugin [#47](https://github.com/datagouv/grist-plugin-opendata/pull/47).
- **Mise à jour de l'environnement de développement** :
    - Passage à Node 24 [#45](https://github.com/datagouv/grist-plugin-opendata/pull/45).
    - Mise à jour des outils de qualité de code (TypeScript, ESLint) et de la configuration du projet (passage au format module).

### Autres changements
- **Documentation** : Simplification des instructions d'installation en supprimant les étapes obsolètes concernant la configuration manuelle du fichier `.env`.
- **Nettoyage** : Suppression des résidus de migrations et des options de configuration inutilisées dans le fichier `tsconfig`.
