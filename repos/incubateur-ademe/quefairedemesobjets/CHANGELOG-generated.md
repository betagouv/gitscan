## Changelog : quefairedemesobjets (30 derniers jours, au 07/10/2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante avec le déploiement de la nouvelle version de l'assistant et l'ajout de nouveaux contenus (portail SINOE, éco-organisme LEKO). Les efforts se sont également concentrés sur l'amélioration de la recherche, la correction de l'affichage sur mobile et une optimisation majeure de l'infrastructure pour garantir une meilleure stabilité et performance.

### Évolutions fonctionnelles
- **Assistant & Aide à la décision** :
    - Déploiement de l'Assistant V2 avec redirection automatique des utilisateurs existants [#3480](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3480).
    - Simplification des boutons de partage de l'assistant [#3354](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3354).
- **Recherche & Navigation** :
    - Amélioration de la pertinence des résultats de recherche (scoring) [#3388](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3388).
    - Correction du positionnement des suggestions d'autocomplétion sur mobile iOS [#3380](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3380).
    - Correction d'un bug sur le bouton "précédent" dans les formulaires [#3433](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3433).
- **Contenu & Interface** :
    - Intégration du nouveau portail SINOE [#3312](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3312) et de l'éco-organisme LEKO [#3401](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3401).
    - Amélioration de l'affichage des cartes (intégration de cartes sur mesure dans des fenêtres modales) [#3071](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3071).
    - Restauration du style visuel de l'administration Django [#3410](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3410).
    - Ajout d'un champ de localisation dans le formulaire de contact [#3300](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3300).
    - Ajustements cosmétiques : les informations de tri sont désormais décoratives par défaut [#3403](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3403) et correction de l'orientation du mode liste pour les visiteurs [#3411](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3411).

### Évolutions techniques
- **Infrastructure & Performance** :
    - Migration des bases de données Airflow et de l'instance Metabase vers Scaleway [#3384](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3384).
    - Optimisation des performances Docker pour les bases de données PostGIS [#3376](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3376).
    - Fine-tuning des configurations Nginx et Gunicorn pour améliorer la réactivité du serveur [#3373](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3373).
- **Développement & Architecture** :
    - Migration des produits "legacy" de Django vers Wagtail pour une meilleure gestion de contenu [#3160](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3160).
    - Refactoring du module API pour centraliser les paramètres des workers [#3463](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3463).
    - Déplacement de modèles de données dans le pipeline dbt pour une meilleure organisation [#3386](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3386).
- **Sécurité & DevOps** :
    - Mise en place d'une procédure de rotation des mots de passe [#3382](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3382).
    - Sécurisation des commandes de base de données (psql, ogr2ogr) via l'utilisation de variables d'environnement pour les secrets [#3448](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3448).
    - Amélioration de la gestion des environnements de preview (nettoyage automatique des PR fermées) [#3385](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3385).
    - Ajout d'un monitoring pour le proxy PostHog [#3374](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3374).
- **Tests** :
    - Correction et stabilisation des tests de bout en bout (E2E) suite aux évolutions de la recherche [#3471](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3471) et simplification de la génération de la base de données locale [#3397](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3397).

### Autres changements
- Nettoyage du code (suppression de code mort) [#3408](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3408).
- Mise à jour du fichier `.gitignore` pour inclure le cache Parcel.
- Ajustement de la configuration Dependabot pour exclure les versions de TypeScript supérieures à 7 [#3375](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3375).
