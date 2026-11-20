## Changelog : histologe (30 derniers jours, au 19/11/2026)

### Résumé
Ce mois-ci, les développements ont principalement porté sur l'amélioration de l'accessibilité numérique (formulaires et statistiques) et le renforcement de la sécurité du système. Des avancées significatives ont été réalisées sur l'interconnexion avec des partenaires externes (BAN, Nantes Métropole) et sur l'optimisation des processus d'import/export de données pour les agents.

### Évolutions fonctionnelles
- **Accessibilité & Expérience Utilisateur (UX) :**
    - Amélioration de l'accessibilité des formulaires usagers (gestion des erreurs, regroupement de champs, aide à la saisie et choix des catégories) [#6622](https://github.com/MTES-MCT/histologe/issues/6622), [#6621](https://github.com/MTES-MCT/histologe/issues/6621), [#6619](https://github.com/MTES-MCT/histologe/issues/6619).
    - Optimisation de la navigation au clavier et de la hiérarchie visuelle pour les pages de statistiques [#6642](https://github.com/MTES-MCT/histologe/issues/6642), [#6624](https://github.com/MTES-MCT/histologe/issues/6624).
    - Améliorations de l'interface : boutons responsives [#6605](https://github.com/MTES-MCT/histologe/issues/6605), titres de pages explicites [#6626](https://github.com/MTES-MCT/histologe/issues/6626) et remplacement du lien de déconnexion par un bouton [#6625](https://github.com/MTES-MCT/histologe/issues/6625).
- **Gestion des données & Interconnexions :**
    - Mise en place de la connexion OAuth 2 avec Nantes Métropole (SCHS) [#6473](https://github.com/MTES-MCT/histologe/issues/6473).
    - Utilisation de l'API BAN pour la validation automatique des codes postaux et communes [#6693](https://github.com/MTES-MCT/histologe/issues/6693).
    - Optimisation des imports/exports (gestion des caractères invisibles Excel, nouvelles colonnes d'export, migration des arrêtés santé habitat) [#6564](https://github.com/MTES-MCT/histologe/issues/6564), [#6550](https://github.com/MTES-MCT/histologe/issues/6550), [#6543](https://github.com/MTES-MCT/histologe/issues/6543), [#6563](https://github.com/MTES-MCT/histologe/issues/6563).
- **Pilotage & Back-Office (BO) :**
    - Centralisation des outils pour les RT via un menu unique "Mes outils" [#6679](https://github.com/MTES-MCT/histologe/issues/6679).
    - Nouveaux filtres et fonctionnalités de gestion (filtre Provenance, affectation des bailleurs sociaux, gestion des types de documents via IA) [#6656](https://github.com/MTES-MCT/histologe/issues/6656), [#6649](https://github.com/MTES-MCT/histologe/issues/6649), [#6446](https://github.com/MTES-MCT/histologe/issues/6446).
    - Ajustements des règles de signalement (logique de réponse, gestion des adresses, édition des heures de visite) [#6549](https://github.com/MTES-MCT/histologe/issues/6549), [#6574](https://github.com/MTES-MCT/histologe/issues/6574), [#6635](https://github.com/MTES-MCT/histologe/issues/6635).
- **Sécurité & Accès :**
    - Notifications de connexion lors de changements de session [#6661](https://github.com/MTES-MCT/histologe/issues/6661).
    - Blocage des accès sur les signalements archivés [#6544](https://github.com/MTES-MCT/histologe/issues/6544).
    - Ouverture des notes et étiquettes personnelles à l'ensemble des utilisateurs [#6680](https://github.com/MTES-MCT/histologe/issues/6680).

### Évolutions techniques
- **Sécurité :**
    - Mise en place du WAF OGO [#6650](https://github.com/MTES-MCT/histologe/issues/6650).
    - Renforcement de la sécurité (protection de l'export PDF, postmortem YesWeHack, correction des voters) [#6719](https://github.com/MTES-MCT/histologe/issues/6719), [#6724](https://github.com/MTES-MCT/histologe/issues/6724), [#6700](https://github.com/MTES-MCT/histologe/issues/6700).
    - Mise à jour de la politique de référent (`referrer-policy`) [#6662](https://github.com/MTES-MCT/histologe/issues/6662).
- **Infrastructure & CI/CD :**
    - Ajout d'un nouveau workflow PHP dans la CI [#6638](https://github.com/MTES-MCT/histologe/issues/6638).
    - Mise en place d'une surveillance Metabase [#6616](https://github.com/MTES-MCT/histologe/issues/6616).
- **Maintenance & Optimisation :**
    - Mise à jour de Symfony (8.1.11) [#6640](https://github.com/MTES-MCT/histologe/issues/6640).
    - Refactorisation du code des statistiques [#6581](https://github.com/MTES-MCT/histologe/issues/6581).
    - Améliorations techniques diverses (gestion des routes par rôle, intégration d'iframe-resizer, gestion des millisecondes dans les dates EXIF) [#6727](https://github.com/MTES-MCT/histologe/issues/6727), [#6603](https://github.com/MTES-MCT/histologe/issues/6603), [#6536](https://github.com/MTES-MCT/histologe/issues/6536).
    - Nettoyage des dépréciations et avertissements dans le code [#6697](https://github.com/MTES-MCT/histologe/issues/6697).

### Autres changements
- Nettoyage de code (suppression d'erreurs de niveau 8 Stan) [#6628](https://github.com/MTES-MCT/histologe/issues/6628).
