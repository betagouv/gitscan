## Changelog : infra (30 derniers jours, au 15 octobre 2026)

### Résumé
Ce mois-ci, l'infrastructure a franchi une étape importante vers plus de sécurité et d'autonomie. Les principaux changements concernent le déploiement d'un réseau privé pour isoler les services de production et la mise en place de serveurs d'exécution (runners) dédiés pour l'automatisation. L'outil d'analyse Matomo a également été intégré à l'écosystème.

### Évolutions fonctionnelles
- Intégration de l'outil d'analyse Matomo [#235](https://github.com/mission-apprentissage/infra/pull/235).

### Évolutions techniques
- **Infrastructure privée et réseau :**
    - Mise en œuvre de mécanismes pour supporter l'infrastructure privée [#237](https://github.com/mission-apprentissage/infra/pull/237).
    - Déploiement de `bal.production` sur un réseau privé.
    - Configuration de serveurs virtuels (vhosts) Nginx pour les serveurs privés [#238](https://github.com/mission-apprentissage/infra/pull/238).
    - Ajustements des règles de pare-feu (Nftables) et des configurations VLAN pour les environnements de staging et de production.
- **CI/CD et automatisation :**
    - Mise en place de runners GitHub auto-hébergés [#236](https://github.com/mission-apprentissage/infra/pull/236).
    - Sécurisation des runners via l'importation des clés OpenPGP des dépôts directement dans les conteneurs.
    - Mise à jour de l'image Docker utilisée par les runners.
- **Disponibilité et maintenance :**
    - Exclusion de `bal.production` des cycles de redémarrage automatique programmés afin de garantir une disponibilité continue.

### Autres changements
- Corrections de diverses fautes de frappe dans la documentation et les fichiers de configuration.
