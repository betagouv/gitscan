## Changelog : aides-agri (30 derniers jours, au 9 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité du site, avec l'ajout d'une politique de sécurité et la correction de vulnérabilités. Des améliorations ont également été apportées à l'interface d'administration pour faciliter la gestion des aides, notamment la duplication d'aides et l'export de données. Enfin, plusieurs dépendances ont été mises à jour pour bénéficier des dernières corrections et fonctionnalités.

### Évolutions fonctionnelles
- **Administration :** Possibilité de dupliquer une aide existante depuis l'interface d'administration. [#448](https://github.com/betagouv/aides-agri/issues/448)
- **Administration :** Réorganisation des champs dans le formulaire d'édition d'une aide pour une meilleure ergonomie. [#446](https://github.com/betagouv/aides-agri/issues/446)
- **Administration :** Ajout de la possibilité d'exporter les données de toutes les tables de référence au format CSV. [#424](https://github.com/betagouv/aides-agri/issues/424)
- **Interface utilisateur :** Correction de la mise en page lors de l'impression de la recommandation. [#425](https://github.com/betagouv/aides-agri/issues/425)
- **Interface utilisateur :** Ajout d'une mention de non-opposabilité sur les fiches d'aides. [#432](https://github.com/betagouv/aides-agri/issues/432)
- **Statistiques :** Ajout d'une page de statistiques basée sur la matrice d'impact. [#413](https://github.com/betagouv/aides-agri/issues/413)
- **Filtres :** Correction d'un bug sur le filtre d'aides par zone géographique. [#423](https://github.com/betagouv/aides-agri/issues/423)

### Évolutions techniques
- **Sécurité :** Correction d'une vulnérabilité open-redirection. [#441](https://github.com/betagouv/aides-agri/issues/441) et [#442](https://github.com/betagouv/aides-agri/issues/442)
- **Sécurité :** Mise en place d'une surveillance des attaques brute-force. [#440](https://github.com/betagouv/aides-agri/issues/440)
- **Sécurité :** Ajout d'un fichier `security.txt` pour la divulgation responsable des vulnérabilités. [#414](https://github.com/betagouv/aides-agri/issues/414) et [#415](https://github.com/betagouv/aides-agri/issues/415)
- **Dépendances :** Mise à jour de Django-DSFR vers la version 3.4.0. [#459](https://github.com/betagouv/aides-agri/issues/459)
- **CI/CD :** Optimisation du workflow Github. [#467](https://github.com/betagouv/aides-agri/issues/467)
- **CI/CD :** Mise à jour de certaines actions Github pour éviter les avertissements liés à Node.js 20. [#436](https://github.com/betagouv/aides-agri/issues/436)

### Autres changements
- **Documentation :** Ajout de tests sur l'export CSV dans l'admin. [#438](https://github.com/betagouv/aides-agri/issues/438)
- **Code :** Obfuscation des données personnelles dans la base de données après l'envoi d'un email. [#439](https://github.com/betagouv/aides-agri/issues/439)
- **Code :** Diverses petites améliorations et corrections mineures. [#419](https://github.com/betagouv/aides-agri/issues/419), [#420](https://github.com/betagouv/aides-agri/issues/420), [#421](https://github.com/betagouv/aides-agri/issues/421)
- **Configuration :** Déplacement de l'information légale en bas de la page Aide. [#466](https://github.com/betagouv/aides-agri/issues/466)
