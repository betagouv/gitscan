## Changelog : vizeau (30 derniers jours, au 23 juillet 2026)

### Résumé
Les dernières mises à jour de Vizeau se concentrent sur l'amélioration de l'expérience utilisateur, la correction de bugs et la modernisation de l'infrastructure technique. Une migration vers AdonisJS 7 a été réalisée, apportant des améliorations de performance et de sécurité. De nouvelles fonctionnalités ont été ajoutées, notamment l'affichage des projets sur la carte et l'intégration de Matomo pour le suivi analytique.

### Évolutions fonctionnelles
- Affichage des projets sur les pop-ups de parcelle sur la carte. [#467](https://github.com/MTES-MCT/vizeau/pull/467)
- Amélioration du message d'erreur d'authentification pour une meilleure clarté. [#472](https://github.com/MTES-MCT/vizeau/pull/472)
- Correction d'une permission trop stricte empêchant le téléchargement de documents de journal de bord. [#477](https://github.com/MTES-MCT/vizeau/pull/477)
- Les commentaires de parcelle sont maintenant individuels à chaque utilisateur. [#474](https://github.com/MTES-MCT/vizeau/pull/474)
- Intégration de Matomo pour le suivi analytique et la collecte de données d'utilisation. [#459](https://github.com/MTES-MCT/vizeau/pull/459)
- Amélioration de l'interface utilisateur (UI) avec des corrections basées sur les retours Figma. [#462](https://github.com/MTES-MCT/vizeau/pull/462)
- Scripts pour la génération de fiches AAC et d'analyses. [#460](https://github.com/MTES-MCT/vizeau/pull/460) & [#458](https://github.com/MTES-MCT/vizeau/pull/458)

### Évolutions techniques
- Migration vers AdonisJS 7 pour bénéficier des dernières améliorations et corrections de sécurité. [#470](https://github.com/MTES-MCT/vizeau/pull/470)
- Refonte du système de routage avec l'utilisation d'un nouveau router. [#478](https://github.com/MTES-MCT/vizeau/pull/478)
- Utilisation de "barrel" pour les contrôleurs afin d'améliorer l'organisation du code. [#476](https://github.com/MTES-MCT/vizeau/pull/476)
- Simplification des modèles de données.
- Optimisation de la requête de récupération des AAC et ajout d'un mode debug pour DuckDB. [#461](https://github.com/MTES-MCT/vizeau/pull/461)
- Génération de tuiles PMTiles. [#369](https://github.com/MTES-MCT/vizeau/pull/369)

### Autres changements
- Ajout d'un fichier `.gitignore` et d'un fichier `.env.sample`.
- Mise à jour des dépendances (TailwindCSS, npm).
- Corrections de linter (imports de type).
- Amélioration de la taille d'une illustration sur la page d'accueil.
- Corrections diverses et amélioration de la qualité du code suite aux revues.
