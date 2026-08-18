## Changelog : code-du-travail-numerique (30 derniers jours, au 14 août 2026)

### Résumé
Les dernières évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment via l'optimisation des parcours de contribution et du système de collecte d'avis (NPS). La navigation a été affinée et les outils de contact ont été enrichis pour mieux répondre aux besoins des usagers, tout en renforçant la précision des données analytiques.

### Évolutions fonctionnelles
- **Amélioration du parcours de contribution** : réduction de la taille des titres de réponse [#7439](https://github.com/SocialGouv/code-du-travail-numerique/issues/7439), ajout de liens vers des pages personnalisées [#7434](https://github.com/SocialGouv/code-du-travail-numerique/issues/7434), affichage des thèmes et sous-thèmes en haut des pages [#7393](https://github.com/SocialGouv/code-du-travail-numerique/issues/7393) et optimisation de la modale des conventions collectives [#7389](https://github.com/SocialGouv/code-du-travail-numerique/issues/7389).
- **Navigation et SEO** : mise en place d'un nouveau fil d'Ariane pour les contenus natifs [#7378](https://github.com/SocialGouv/code-du-travail-numerique/issues/7378).
- **Contact** : ajout d'un questionnaire spécifique pour le canal téléphonique [#7418](https://github.com/SocialGouv/code-du-travail-numerique/issues/7418).
- **Expérience utilisateur (NPS)** : intégration du score NPS directement sur le site [#7382](https://github.com/SocialGouv/code-du-travail-numerique/issues/7382) et optimisation de la fréquence et du comportement de la fenêtre de sollicitation [#7433](https://github.com/SocialGouv/code-du-travail-numerique/issues/7433) [#7416](https://github.com/SocialGouv/code-du-travail-numerique/issues/7416) [#7406](https://github.com/SocialGouv/code-du-travail-numerique/issues/7406).
- **Partage** : retrait du bloc de partage sur la majorité des pages, conservé uniquement pour les actualités [#7392](https://github.com/SocialGouv/code-du-travail-numerique/issues/7392).

### Évolutions techniques
- **Fiabilisation des données** : utilisation de Zod pour la validation des entrées des APIs [#7407](https://github.com/SocialGouv/code-du-travail-numerique/issues/7407).
- **Analyse et tracking** : amélioration de la précision du suivi Matomo via le nettoyage des URLs [#7409](https://github.com/SocialGouv/code-du-travail-numerique/issues/7409), le suivi du nombre de conventions collectives trouvées [#7428](https://github.com/SocialGouv/code-du-travail-numerique/issues/7428) et le suivi de la complétion des contributions [#7426](https://github.com/SocialGouv/code-du-travail-numerique/issues/7426) [#7427](https://github.com/SocialGouv/code-du-travail-numerique/issues/7427).
- **Infrastructure et CI/CD** : correction du processus de publication NPM pour absorber les erreurs de signature [#7420](https://github.com/SocialGouv/code-du-travail-numerique/issues/7420).
- **Refactoring** : réécriture du composant de fil d'Ariane [#7378](https://github.com/SocialGouv/code-du-travail-numerique/issues/7378).
