## Changelog : bhasile (30 derniers jours, au 26 octobre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de la précision des statistiques et de l'expérience cartographique. La sécurité a été renforcée, notamment par l'imposition de l'authentification multi-facteurs (MFA), et l'interface utilisateur a été affinée pour offrir une meilleure navigation et des données plus lisibles.

### Évolutions fonctionnelles
- **Statistiques et rapports** : Amélioration de la gestion des statistiques pour les années incomplètes [#1705](https://github.com/betagouv/bhasile/issues/1705), corrections de l'affichage des statistiques publiques [#1709](https://github.com/betagouv/bhasile/issues/1709), [#1708](https://github.com/betagouv/bhasile/issues/1708) et suppression de la note moyenne [#1696](https://github.com/betagouv/bhasile/issues/1696).
- **Cartographie** : Ajout de la localisation des adresses et affichage des communes sur la carte [#1680](https://github.com/betagouv/bhasile/issues/1680), [#1686](https://github.com/betagouv/bhasile/issues/1686).
- **Interface utilisateur** : 
    - Ajout d'une fonction de recherche dans le filtre par département [#1700](https://github.com/betagouv/bhasile/issues/1700).
    - Affichage des pourcentages dans le tableau des lieux [#1735](https://github.com/betagouv/bhasile/issues/1735).
    - Restauration du tableau de bord et des filtres [#1691](https://github.com/betagouv/bhasile/issues/1691), [#1693](https://github.com/betagouv/bhasile/issues/1693).
    - Ajout d'un lien vers le centre d'aide [#1699](https://github.com/betagouv/bhasile/issues/1699).
- **Gestion métier (CPOM et structures)** : 
    - Les indicateurs financiers sont désormais optionnels pour les années dans les CPOM [#1717](https://github.com/betagouv/bhasile/issues/1717).
    - Conservation des structures fermées dans les descriptions de CPOM [#1707](https://github.com/betagouv/bhasile/issues/1707).
    - Évolution de la terminologie "Ofii" vers "opérateur" (v2) [#1692](https://github.com/betagouv/bhasile/issues/1692).
    - Suppression du formulaire de récupération d'adresses [#1716](https://github.com/betagouv/bhasile/issues/1716).

### Évolutions techniques
- **Sécurité et accès** : 
    - Imposition du MFA sur ProConnect [#1712](https://github.com/betagouv/bhasile/issues/1712).
    - Évolution de la gestion des rôles et des périmètres d'accès [#1694](https://github.com/betagouv/bhasile/issues/1694).
    - Renforcement du contrôle des routes (PUT) pour les CPOM et opérateurs [#1731](https://github.com/betagouv/bhasile/issues/1731) et filtrage des lectures par subventions [#1721](https://github.com/betagouv/bhasile/issues/1721).
- **Infrastructure et CI/CD** : 
    - Mise à jour du framework Next.js [#1740](https://github.com/betagouv/bhasile/issues/1740).
    - Migration des ressources vers S3 [#1661](https://github.com/betagouv/bhasile/issues/1661) et mise à jour de l'image MinIO en CI [#1695](https://github.com/betagouv/bhasile/issues/1695).
    - Résolution de problèmes liés au build [#1710](https://github.com/betagouv/bhasile/issues/1710).
- **Maintenance et Qualité** : 
    - Refactorisation du module de cartographie [#1681](https://github.com/betagouv/bhasile/issues/1681).
    - Amélioration et correction des tests unitaires et E2E [#1726](https://github.com/betagouv/bhasile/issues/1726), [#1725](https://github.com/betagouv/bhasile/issues/1725), [#1727](https://github.com/betagouv/bhasile/issues/1727).
    - Amélioration des logs pour le diagnostic des problèmes de fichiers [#1732](https://github.com/betagouv/bhasile/issues/1732).

### Autres changements
- Amélioration de la FAQ [#1729](https://github.com/betagouv/bhasile/issues/1729).
- Nettoyage de données (anciennes subventions et suppression des filiales) [#1711](https://github.com/betagouv/bhasile/issues/1711), [#1723](https://github.com/betagouv/bhasile/issues/1723).
- Corrections de diverses fautes de frappe [#1730](https://github.com/betagouv/bhasile/issues/1730).
