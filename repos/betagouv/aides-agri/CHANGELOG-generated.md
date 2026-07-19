## Changelog : aides-agri (30 derniers jours, au 11 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de nouvelles régions géographiques couvertes par le service, l'amélioration de l'expérience utilisateur dans l'administration (export CSV, gestion des retours utilisateurs), et des corrections de bugs notamment concernant le tracking et les liens. Une migration vers Python 3.14 a également été effectuée.

### Évolutions fonctionnelles
- Ajout de la région Normandie aux régions couvertes par le service. [#667](https://github.com/betagouv/aides-agri/issues/667)
- Ajout de la région Bourgogne-Franche-Comté aux régions couvertes par le service. [#632](https://github.com/betagouv/aides-agri/issues/632)
- Correction du lien vers le formulaire de collecte des aides. [#649](https://github.com/betagouv/aides-agri/issues/649)
- Améliorations de l'interface d'administration des retours utilisateurs. [#646](https://github.com/betagouv/aides-agri/issues/646)
- Application des filtres lors de l'export CSV des aides depuis l'administration. [#643](https://github.com/betagouv/aides-agri/issues/643)
- Correction du tracking des liens externes. [#630](https://github.com/betagouv/aides-agri/issues/630)
- Les liens non cliquables ne sont plus affichés dans la liste des résultats. [#629](https://github.com/betagouv/aides-agri/issues/629)
- Possibilité d'appliquer les changements d’une fiche mère à tous les niveaux en-dessous d’elle. [#665](https://github.com/betagouv/aides-agri/issues/665)

### Évolutions techniques
- Migration vers Python 3.14. [#644](https://github.com/betagouv/aides-agri/issues/644)
- Rendre l’export CSV depuis le back-office asynchrone pour améliorer la performance. [#662](https://github.com/betagouv/aides-agri/issues/662)
- Tentative de réduction de l'empreinte mémoire de la page de résultats. [#652](https://github.com/betagouv/aides-agri/issues/652) et [#647](https://github.com/betagouv/aides-agri/issues/647)
- Mise à jour de Django de la version 5.2.15 à 5.2.16. [#666](https://github.com/betagouv/aides-agri/issues/666)
- Script de création rétroactive des releases Github. [#657](https://github.com/betagouv/aides-agri/issues/657)
- Correction d’une faille de sécurité. [#661](https://github.com/betagouv/aides-agri/issues/661)

### Autres changements
- Alerte à l’équipe en cas d’organisme sans logo ayant des aides publiées. [#664](https://github.com/betagouv/aides-agri/issues/664)
- Mise à jour des CGU et de la politique de confidentialité en vue des alertes mail. [#660](https://github.com/betagouv/aides-agri/issues/660)
- Ajout de documentation d'infrastructure concernant les variables d'environnement. [#633](https://github.com/betagouv/aides-agri/issues/633)
- Mise à jour des statistiques pour juin 2026. [#648](https://github.com/betagouv/aides-agri/issues/648)
- Rétablissement de la taille des champs dans l'administration. [#645](https://github.com/betagouv/aides-agri/issues/645)
