## Changelog : mon-indemnisation-justice (30 derniers jours, au 04/09/2026)

### Résumé
Ce mois-ci, les développements ont principalement porté sur la fiabilisation du parcours de demande d'indemnisation (notamment pour les dossiers de bris de porte) et la correction d'anomalies liées à la gestion des dates et des affectations. Parallèlement, une mise à jour majeure de l'environnement technique a été réalisée pour garantir la pérennité et la performance de l'application.

### Évolutions fonctionnelles
- Correction des doublons lors de l'affectation des dossiers [#163](https://github.com/betagouv/mon-indemnisation-justice/pull/163).
- Amélioration du module "bris de porte" : correction des trames de documents [#154](https://github.com/betagouv/mon-indemnisation-justice/pull/154) et optimisation de la gestion des pièces justificatives [#160](https://github.com/betagouv/mon-indemnisation-justice/pull/160).
- Détection et remontée d'erreurs lors de l'impression de documents [#162](https://github.com/betagouv/mon-indemnisation-justice/pull/162).
- Résolution de dysfonctionnements liés aux tests d'éligibilité [#151](https://github.com/betagouv/mon-indemnisation-justice/pull/151).
- Fiabilisation de la gestion des dates lors du marquage d'un dossier comme "indemnisé".
- Amélioration de l'ergonomie pour les agents FDO avec la possibilité de se déconnecter directement depuis la modale d'affectation.
- Uniformisation des paragraphes relatifs à la responsabilité.

### Évolutions techniques
- Mise à jour majeure de l'infrastructure logicielle : passage à PHP 8.5, Symfony 8.1 et Node.js v24 [#158](https://github.com/betagouv/mon-indemnisation-justice/pull/158).
- Actualisation des versions des GitHub Actions.
- Correction d'un problème de remontée de données (Sentry) concernant l'exactitude des dates.
- Ajustement des tests unitaires suite aux montées de version des composants.
