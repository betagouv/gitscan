## Changelog : ma-cantine (30 derniers jours, au 19 août 2026)

### Résumé
Ce mois-ci, la plateforme a connu une refonte majeure de l'espace "Établissement" avec l'introduction de nouvelles pages de gestion (informations, page publique, gestionnaires) et une interface plus intuitive et accessible. Les outils de diagnostic ont été enrichis avec de nouveaux indicateurs de provenance des aliments et des règles de contrôle plus strictes pour garantir la qualité des données. Enfin, l'infrastructure technique et les capacités de l'API ont été considérablement renforcées pour améliorer la performance et la fiabilité du service.

### Évolutions fonctionnelles
- **Gestion des Établissements :** 
    - Refonte de l'interface avec de nouvelles pages dédiées : "Mes informations" (remplaçant "Gérer mon établissement") [#6902](https://github.com/betagouv/ma-cantine/issues/6902), "Ma page publique" [#6921](https://github.com/betagouv/ma-cantine/issues/6921), "Cantine du groupe" [#6906](https://github.com/betagouv/ma-cantine/issues/6906), "Toutes mes télédéclarations" [#6907](https://github.com/betagouv/ma-cantine/issues/6907) et "Mes gestionnaires" [#6909](https://github.com/betagouv/ma-cantine/issues/6909).
    - Améliorations de l'expérience utilisateur : interface responsive [#6947](https://github.com/betagouv/ma-cantine/issues/6947), meilleure accessibilité [#6948](https://github.com/betagouv/ma-cantine/issues/6948), affichage clair des champs en erreur [#6934](https://github.com/betagouv/ma-cantine/issues/6934) et pagination dynamique des tableaux [#6950](https://github.com/betagouv/ma-cantine/issues/6950).
- **Diagnostics :** 
    - Ajout de nouveaux indicateurs de provenance (France, Europe, circuit court, local, etc.) et de détails par famille d'aliments (AOC/AOP, IGP, STG) [#7021](https://github.com/betagouv/ma-cantine/issues/7021) [#7019](https://github.com/betagouv/ma-cantine/issues/7019) [#7006](https://github.com/betagouv/ma-cantine/issues/7006).
    - Introduction du champ obligatoire `nombre_repas_an` pour 2026 [#7010](https://github.com/betagouv/ma-cantine/issues/7010).
    - Renforcement des règles métier pour assurer la cohérence des données saisies (ex: cohérence des totaux et des labels bio/équitable) [#7012](https://github.com/betagouv/ma-cantine/issues/7012) [#7007](https://github.com/betagouv/ma-cantine/issues/7007) [#7004](https://github.com/betagouv/ma-cantine/issues/7004).
- **Bilans & Télédéclarations :** 
    - Ajout de liens directs vers les arrêtés Legifrance pour chaque année de campagne [#7014](https://github.com/betagouv/ma-cantine/issues/7014).
    - Amélioration de la consultation des justificatifs PDF [#6958](https://github.com/betagouv/ma-cantine/issues/6958).
- **Administration & Recherche :** 
    - Amélioration de la recherche par commune et SIREN [#6976](https://github.com/betagouv/ma-cantine/issues/6976).
    - Nouvelles fonctionnalités d'administration : boutons "Restaurer" pour les achats et cantines archivés [#6979](https://github.com/betagouv/ma-cantine/issues/6979) [#6952](https://github.com/betagouv/ma-cantine/issues/6952) et gestion simplifiée des logos [#6932](https://github.com/betagouv/ma-cantine/issues/6932).
    - Mise à jour visuelle des badges [#6982](https://github.com/betagouv/ma-cantine/issues/6982).

### Évolutions techniques
- **API :** 
    - Extension et optimisation des endpoints pour les Achats (split du `/summary`) [#7042](https://github.com/betagouv/ma-cantine/issues/7042), les Diagnostics (nouveaux endpoints `/check` et `/recap`) [#6991](https://github.com/betagouv/ma-cantine/issues/6991) [#7023](https://github.com/betagouv/ma-cantine/issues/7023), les Bilans [#6975](https://github.com/betagouv/ma-cantine/issues/6975) [#6974](https://github.com/betagouv/ma-cantine/issues/6974) et la gestion complète des images/logos [#6933](https://github.com/betagouv/ma-cantine/issues/6933) [#6935](https://github.com/betagouv/ma-cantine/issues/6935).
- **Infrastructure & Stockage :** Correction de la configuration de stockage S3 suite à la mise à jour de la bibliothèque `boto3` [#7039](https://github.com/betagouv/ma-cantine/issues/7039) [#7028](https://github.com/betagouv/ma-cantine/issues/7028).
- **Architecture & Code :** 
    - Refactorisation de la gestion des applications Django pour une meilleure séparation des configurations [#7033](https://github.com/betagouv/ma-cantine/issues/7033).
    - Amélioration de l'architecture frontend (nouveau store et router pour la gestion du layout) [#6959](https://github.com/betagouv/ma-cantine/issues/6959).
    - Homogénéisation des tests de l'API [#6944](https://github.com/betagouv/ma-cantine/issues/6944).
    - Nettoyage de l'ancien code lié aux pages d'établissements supprimées [#6946](https://github.com/betagouv/ma-cantine/issues/6946).

### Autres changements
- Nettoyage et organisation des dépendances dans le fichier `pyproject.toml` [#6985](https://github.com/betagouv/ma-cantine/issues/6985) [#6791](https://github.com/betagouv/ma-cantine/issues/6791).
