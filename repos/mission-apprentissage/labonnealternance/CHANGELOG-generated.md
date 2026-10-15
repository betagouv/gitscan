## Changelog : labonnealternance (30 derniers jours, au 14 octobre 2026)

### Résumé
Ce mois a été marqué par le lancement majeur du module "Offres Libres", permettant la publication d'offres avec une modération assistée par intelligence artificielle. Parallèlement, un effort massif a été déployé pour améliorer l'accessibilité de la plateforme (conformité RGAA) et refondre l'architecture de recherche pour garantir une meilleure performance et fiabilité des résultats.

### Évolutions fonctionnelles
- **Lancement des Offres Libres** : Mise en place du MVP incluant le dépôt d'offres, la validation de la charte et un système de modération par IA pour garantir la qualité des contenus ([#5078](https://github.com/mission-apprentissage/labonnealternance/issues/5078)).
- **Accessibilité (RGAA)** : Améliorations significatives sur l'ensemble des parcours pour respecter les normes d'accessibilité : formulaires (connexion, création de compte, simulateur, désinscription, feedback), filtres de recherche, et gestion des images/icônes ([#5674](https://github.com/mission-apprentissage/labonnealternance/issues/5674), [#5631](https://github.com/mission-apprentissage/labonnealternance/issues/5631), [#5617](https://github.com/mission-apprentissage/labonnealternance/issues/5617), [#5621](https://github.com/mission-apprentissage/labonnealternance/issues/5621), [#5615](https://github.com/mission-apprentissage/labonnealternance/issues/5615), [#5600](https://github.com/mission-apprentissage/labonnealternance/issues/5600), [#5601](https://github.com/mission-apprentissage/labonnealternance/issues/5601), [#5622](https://github.com/mission-apprentissage/labonnealternance/issues/5622), [#5614](https://github.com/mission-apprentissage/labonnealternance/issues/5614), [#5580](https://github.com/mission-apprentissage/labonnealternance/issues/5580), [#5543](https://github.com/mission-apprentissage/labonnealternance/issues/5543), [#5494](https://github.com/mission-apprentissage/labonnealternance/issues/5494), [#5483](https://github.com/mission-apprentissage/labonnealternance/issues/5483), [#5396](https://github.com/mission-apprentissage/labonnealternance/issues/5396)).
- **Expérience Utilisateur (UX)** :
    - Ajout de nouveaux formulaires de feedback ([#5530](https://github.com/mission-apprentissage/labonnealternance/issues/5530)).
    - Amélioration de la recherche : nouvelles pages diplômes, mise à jour de la cartographie CFA et filtrage des offres redirigeant vers DirectEmploi ([#5548](https://github.com/mission-apprentissage/labonnealternance/issues/5548), [#5660](https://github.com/mission-apprentissage/labonnealternance/issues/5660), [#5661](https://github.com/mission-apprentissage/labonnealternance/issues/5661)).
    - Optimisation SEO via des méta-descriptions dynamiques sur les fiches offres ([#5613](https://github.com/mission-apprentissage/labonnealternance/issues/5613)).
    - Corrections d'interface : gestion du responsive sur mobile, réinitialisation des formulaires et conservation des paramètres de recherche ([#5578](https://github.com/mission-apprentissage/labonnealternance/issues/5578), [#5672](https://github.com/mission-apprentissage/labonnealternance/issues/5672), [#5632](https://github.com/mission-apprentissage/labonnealternance/issues/5632)).
    - Nouvelle option de clôture d'offre : "J'ai reçu assez de candidatures" ([#5501](https://github.com/mission-apprentissage/labonnealternance/issues/5501)).
- **Gestion des données** :
    - Mise en place de la purge automatique des CV après un an de conservation ([#5495](https://github.com/mission-apprentissage/labonnealternance/issues/5495)).
    - Renforcement de la modération via la mise en liste noire de certains CFA ([#5475](https://github.com/mission-apprentissage/labonnealternance/issues/5475), [#5502](https://github.com/mission-apprentissage/labonnealternance/issues/5502)).

### Évolutions techniques
- **Architecture de recherche** : Refonte majeure de l'indexation et de la gestion de l'écriture des données de recherche pour améliorer la fiabilité et les performances ([#5526](https://github.com/mission-apprentissage/labonnealternance/issues/5526), [#5525](https://github.com/mission-apprentissage/labonnealternance/issues/5525), [#5524](https://github.com/mission-apprentissage/labonnealternance/issues/5524)).
- **Intelligence Artificielle** : Développement d'un prototype de classifieur pour la modération automatique des champs libres ([#5497](https://github.com/mission-apprentissage/labonnealternance/issues/5497), [#5496](https://github.com/mission-apprentissage/labonnealternance/issues/5496)).
- **Sécurité et Confidentialité** :
    - Protection des données personnelles : blocage de l'envoi de données sensibles vers Sentry ([#5700](https://github.com/mission-apprentissage/labonnealternance/issues/5700)) et amélioration de l'anonymisation des candidatures ([#5516](https://github.com/mission-apprentissage/labonnealternance/issues/5516)).
    - Sécurisation des logs : suppression des JWT refusés écrits en clair ([#5696](https://github.com/mission-apprentissage/labonnealternance/issues/5696)).
- **Stabilité et Performance** :
    - Résolution de plantages mémoire du processeur de tâches lors de jobs longs ([#5607](https://github.com/mission-apprentissage/labonnealternance/issues/5607)).
    - Amélioration de la gestion des erreurs serveur (codes HTTP plus précis) ([#5663](https://github.com/mission-apprentissage/labonnealternance/issues/5663)).
- **Intégrations et API** :
    - Importation du flux LinkedIn ([#5482](https://github.com/mission-apprentissage/labonnealternance/issues/5482)).
    - Enrichissement de l'API pour les partenaires (endpoints batch pour les liens et la recherche d'entreprises) ([#5562](https://github.com/mission-apprentissage/labonnealternance/issues/5562)).
- **CI/CD** : Automatisation des notifications de déploiement de preview et intégration de CodeQL dans le workflow de revue ([#5657](https://github.com/mission-apprentissage/labonnealternance/issues/5657), [#5568](https://github.com/mission-apprentissage/labonnealternance/issues/5568)).

### Autres changements
- **Documentation** : Mise à jour des conventions de titres de PR, de la documentation de l'IA (Claude/Copilot) et nettoyage des commentaires obsolètes ([#5522](https://github.com/mission-apprentissage/labonnealternance/issues/5522), [#5519](https://github.com/mission-apprentissage/labonnealternance/issues/5519)).
- **Nettoyage** : Suppression de templates inutilisés et de collections de données fantômes ([#5644](https://github.com/mission-apprentissage/labonnealternance/issues/5644), [#5618](https://github.com/mission-apprentissage/labonnealternance/issues/5618)).
