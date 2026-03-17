## Changelog : infra (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à l'infrastructure au cours du dernier mois. Les principales évolutions concernent la migration des secrets vers SOPS pour une meilleure sécurité, des corrections de bugs sur les scripts de redémarrage et de rotation des mots de passe, ainsi que des optimisations de la configuration de certains services comme Fluentd et Nginx.

### Évolutions fonctionnelles
- Lancement des services Docker via `docker-compose.system.yml` lors du déploiement. [#209](https://github.com/mission-apprentissage/infra/issues/209)
- Correction d'un bug sur le script `scheduled-all-servers-reboot.yml` pour assurer le bon redémarrage des serveurs. [#207](https://github.com/mission-apprentissage/infra/issues/207)
- Correction de l'utilisation du profil TLS client par Certbot pour éviter des problèmes de certification. [#198](https://github.com/mission-apprentissage/infra/issues/198)

### Évolutions techniques
- Migration des secrets stockés dans Ansible Vault vers SOPS pour les environnements tdb, lab, monitoring et mongodb. [#206](https://github.com/mission-apprentissage/infra/issues/206), [#203](https://github.com/mission-apprentissage/infra/issues/203), [#196](https://github.com/mission-apprentissage/infra/issues/196), [#195](https://github.com/mission-apprentissage/infra/issues/195), [#194](https://github.com/mission-apprentissage/infra/issues/194)
- Limitation de la mémoire utilisée par le conteneur Docker system. [#199](https://github.com/mission-apprentissage/infra/issues/199)
- Augmentation du nombre de fichiers ouverts par le conteneur Fluentd pour améliorer sa stabilité. [#202](https://github.com/mission-apprentissage/infra/issues/202)
- Mise à jour des images Nginx et ModSecurity-CRS pour bénéficier des dernières corrections de sécurité et améliorations. [#208](https://github.com/mission-apprentissage/infra/issues/208)
- Correction de la limite `MODSEC_REQ_BODY_NOFILES_LIMIT` pour ModSecurity. [#193](https://github.com/mission-apprentissage/infra/issues/193)
- Correction du script `reload.sh` pour Nginx. [#191](https://github.com/mission-apprentissage/infra/issues/191)
- Prise en compte des sous-modules dans les scripts de rotation des mots de passe et de redémarrage. [#204](https://github.com/mission-apprentissage/infra/issues/204)
- Correction de l'utilisation de la variable `TOKEN_MNA_SHARED` dans les scripts de redémarrage des serveurs. [#205](https://github.com/mission-apprentissage/infra/issues/205)
- Correction de l'évaluation des variables SOPS d'habilitations. [#201](https://github.com/mission-apprentissage/infra/issues/201)

### Autres changements
- Décommissionnement de l'environnement pentest. [#200](https://github.com/mission-apprentissage/infra/issues/200)
- Mise à jour de l'inventaire du produit bal. [#192](https://github.com/mission-apprentissage/infra/issues/192)
- Correction d'un bug général. [#197](https://github.com/mission-apprentissage/infra/issues/197)
- Traitement de `disallow` comme un booléen. [#190](https://github.com/mission-apprentissage/infra/issues/190)
