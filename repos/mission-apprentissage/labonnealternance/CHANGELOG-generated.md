## Changelog : labonnealternance (30 derniers jours, au 16/09/2026)

### Résumé
Ce mois a été marqué par une transition majeure vers un nouveau moteur de recherche et une optimisation significative du référencement naturel (SEO). L'application est désormais installable sur mobile via la technologie PWA, offrant une expérience utilisateur plus fluide. Nous avons également renforcé l'accessibilité (RGAA) et enrichi les outils destinés aux recruteurs pour faciliter la mise en relation.

### Évolutions fonctionnelles
- **Recherche et navigation** :
    - Amélioration de la recherche de lieux par département et région [#5248](https://github.com/mission-apprentissage/labonnealternance/issues/5248) ([#5461](https://github.com/mission-apprentissage/labonnealternance/issues/5461)).
    - Unification de la navigation sur les fiches détails avec le nouveau moteur de recherche [#5194](https://github.com/mission-apprentissage/labonnealternance/issues/5194) ([#5212](https://github.com/mission-apprentissage/labonnealternance/issues/5212)).
    - Assouplissement de la recherche de formations pour les liens de formation [#5393](https://github.com/mission-apprentissage/labonnealternance/issues/5393).
    - Restauration du contexte de recherche et des liens lors de la navigation [#5340](https://github.com/mission-apprentissage/labonnealternance/issues/5340) ([#5321](https://github.com/mission-apprentissage/labonnealternance/issues/5321)).
- **Expérience Mobile & PWA** :
    - L'application est désormais installable sur mobile (PWA) [#5221](https://github.com/mission-apprentissage/labonnealternance/issues/5221).
    - Optimisation de la modale de recherche sur mobile (gestion du clavier et affichage) [#5219](https://github.com/mission-apprentissage/labonnealternance/issues/5219).
- **Outils Recruteurs & CFA** :
    - Possibilité de collecter les engagements handicap des recruteurs [#5222](https://github.com/mission-apprentissage/labonnealternance/issues/5222).
    - Intégration de l'étape MER lors du dépôt d'offres rapides [#5162](https://github.com/mission-apprentissage/labonnealternance/issues/5162).
    - Mise en place d'une liste noire pour certains CFA [#5475](https://github.com/mission-apprentissage/labonnealternance/issues/5475).
- **Contenu et Interface** :
    - Amélioration de l'accessibilité (RGAA) sur les images et icônes [#5396](https://github.com/mission-apprentissage/labonnealternance/issues/5396).
    - Création d'une page guide "Recruter un alternant" pour le SEO [#5128](https://github.com/mission-apprentissage/labonnealternance/issues/5128).
    - Mise à jour de la carte des métiers (édition 2026-2027) [#4955](https://github.com/mission-apprentissage/labonnealternance/issues/4955).
    - Ajout de nouveaux partenaires (Apecita) et badges de confiance [#5161](https://github.com/mission-apprentissage/labonnealternance/issues/5161) ([#5263](https://github.com/mission-apprentissage/labonnealternance/issues/5263)).

### Évolutions techniques
- **SEO et Indexation** :
    - Automatisation de la notification des offres via Google Indexing API et IndexNow [#5293](https://github.com/mission-apprentissage/labonnealternance/issues/5293) ([#5271](https://github.com/mission-apprentissage/labonnealternance/issues/5271)).
    - Ajout de données structurées (schema.org) et de balises canonical pour améliorer le référencement [#5270](https://github.com/mission-apprentissage/labonnealternance/issues/5270) ([#5280](https://github.com/mission-apprentissage/labonnealternance/issues/5280)).
- **Performance et Optimisation** :
    - Parallélisation du traitement des liens de formation pour accélérer les temps de réponse [#5204](https://github.com/mission-apprentissage/labonnealternance/issues/5204).
    - Réduction du poids du CSS (DSFR) et optimisation du chargement initial (first-load) [#5179](https://github.com/mission-apprentissage/labonnealternance/issues/5179) ([#5214](https://github.com/mission-apprentissage/labonnealternance/issues/5214)).
    - Mise en place d'un budget de performance dans la CI pour prévenir les régressions [#5191](https://github.com/mission-apprentissage/labonnealternance/issues/5191).
- **Stabilité et Sécurité** :
    - Correction de plusieurs boucles de redirection critiques (espace-pro et layout connecté) [#5383](https://github.com/mission-apprentissage/labonnealternance/issues/5383) ([#5388](https://github.com/mission-apprentissage/labonnealternance/issues/5388)).
    - Renforcement de la sécurité pour empêcher la fuite de secrets vers les outils de monitoring (Sentry) [#5294](https://github.com/mission-apprentissage/labonnealternance/issues/5294).
    - Stabilisation des appels aux services tiers (Mistral, MongoDB) [#5206](https://github.com/mission-apprentissage/labonnealternance/issues/5206).
- **Infrastructure et CI/CD** :
    - Mise à jour de l'environnement (Node 26) et des GitHub Actions [#5335](https://github.com/mission-apprentissage/labonnealternance/issues/5335).
    - Automatisation de la purge du cache du reverse proxy lors des déploiements [#5366](https://github.com/mission-apprentissage/labonnealternance/issues/5366).

### Autres changements
- Nettoyage de la documentation et correction des liens obsolètes [#5213](https://github.com/mission-apprentissage/labonnealternance/issues/5213).
