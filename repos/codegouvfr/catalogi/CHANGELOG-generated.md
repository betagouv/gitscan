## Changelog : catalogi (30 derniers jours, au 10 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur le renforcement des capacités d'administration et l'optimisation des processus d'importation. L'application dispose désormais de nouveaux outils pour configurer l'interface utilisateur et gère plus efficacement les flux de données provenant de sources externes comme Zenodo, HAL ou GitHub.

### Évolutions fonctionnelles
- **Administration de l'interface** : Ajout d'un éditeur de configuration de l'interface utilisateur (UI) accessible via l'API d'administration, permettant de modifier l'apparence de l'outil sans déploiement technique.
- **Gestion des droits** : Restriction de la création de logiciels et ajout de raccourcis dédiés pour les administrateurs.

### Évolutions techniques
- **Optimisation des imports** : Amélioration des performances pour les imports massifs, notamment pour la source Zenodo [#516](https://github.com/codegouvfr/catalogi/issues/516).
- **Fiabilisation des flux de données** : Correction de plusieurs bugs liés à l'importation de données externes :
    - Correction des imports de données HAL [#549](https://github.com/codegouvfr/catalogi/issues/549).
    - Correction de l'importation des utilisateurs depuis GitHub [#550](https://github.com/codegouvfr/catalogi/issues/550).
    - Amélioration de la récupération des organisations via Wikidata.
    - Correction de la gestion des identifiants GitHub et des données ROR (Research Organization Registry).
- **Gestion des données** : 
    - Ajout du champ `lastimport` sur les sources pour un meilleur suivi.
    - Correction de la sauvegarde des descriptions et des données externes en base de données.
- **Maintenance et tests** : 
    - Refactorisation des migrations de base de données.
    - Découplage et amélioration des tests liés à la configuration de l'interface utilisateur.

### Autres changements
- Mises à jour de la version et du build du projet.
