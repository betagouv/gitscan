## Changelog : aigle-api (30 derniers jours, au 15 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface d'administration, notamment pour la gestion des utilisateurs et l'import/export de données. Des corrections ont été apportées pour améliorer la précision des filtres lors du téléchargement de données de parcelles et pour optimiser les performances générales de l'API. La gestion des jeux de tuiles a également été améliorée en modifiant le type de données de la date.

### Évolutions fonctionnelles
- **Interface d'administration :**
    - Possibilité de filtrer les utilisateurs par groupe dans la liste des utilisateurs de l'interface d'administration. [#60](https://github.com/MTES-MCT/aigle-api/pull/60)
    - Ajout de fonctionnalités d'import et d'export de données directement dans l'interface d'administration. [#58](https://github.com/MTES-MCT/aigle-api/pull/58)
- **Téléchargement de parcelles :**
    - Correction d'un bug où les filtres de téléchargement de parcelles n'appliquaient pas correctement les zones personnalisées. [#58](https://github.com/MTES-MCT/aigle-api/pull/58)
    - Correction d'un bug limitant le nombre de détections affichées lors du téléchargement de parcelles. [#58](https://github.com/MTES-MCT/aigle-api/pull/58)
    - Le filtre par défaut pour le score lors du téléchargement de parcelles a été ajusté à 0.3. [#59](https://github.com/MTES-MCT/aigle-api/pull/59)
- **Jeux de tuiles :**
    - Le champ de date des jeux de tuiles est maintenant de type `date` au lieu de `datetime`. [#61](https://github.com/MTES-MCT/aigle-api/pull/61)

### Évolutions techniques
- **Performances :** Améliorations générales des performances de l'API. [#57](https://github.com/MTES-MCT/aigle-api/pull/57)
- **CI/CD :** La chaîne CI ne déploie désormais que si les tests réussissent. [#62](https://github.com/MTES-MCT/aigle-api/pull/62)
- **Logs :** Ajout de logs pour les routes super-admin pour faciliter le débogage. [#61](https://github.com/MTES-MCT/aigle-api/pull/61)
- **Amélioration du setup local :** Amélioration de la configuration pour un développement local plus facile.
- **Bulk import/export :** Amélioration des performances de l'import/export en masse.

### Autres changements
- Modification de la gestion des groupes d'utilisateurs pour les super-administrateurs. [#57](https://github.com/MTES-MCT/aigle-api/pull/57)
- Correction de tests unitaires.
