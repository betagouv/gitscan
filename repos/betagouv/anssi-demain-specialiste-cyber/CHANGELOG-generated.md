## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, le site a connu une refonte majeure de la page d'accueil et des pages associées au challenge "Opération Cactus" et "Passe ton Hack d'abord". De nouvelles sections ont été ajoutées, l'interface a été adaptée pour différents formats d'écran (desktop, tablette) et des corrections de typos ont été apportées. Des améliorations de sécurité ont également été implémentées dans le processus d'intégration continue.

### Évolutions fonctionnelles
- Ajout de la page et du "héros" pour l'opération "Cactus".
- Ajout des sections "Déclarer une action", "Avantages", "Présentation", "Communauté" et "Témoignages" pour l'opération "Cactus".
- Ajout de la section "Plus de CTF".
- Ajout de la page "Passe ton hack d'abord" et de la section "Poursuivez en classe".
- Ajout d'un lien vers le Magistère.
- Adaptation de l'affichage des sections "Comment participer" et "Avantages" pour les écrans tablettes.
- Adaptation de l'affichage des sections "Présentation", "Poursuivez en classe" et "Témoignages" pour les écrans de bureau.
- Ajout d'un lien vers une vidéo.
- Ajout d'un skill pour l'intégration de landing page.

### Évolutions techniques
- Mise en place de mesures de sécurité dans le CI/CD : désactivation des identifiants git des dépôts clonés, validation des configurations et prévention de l'injection de code par 'template expansion' [#7972f7d](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/7972f7d1a526419486782f1234567890abcdef).
- Configuration de Renovate pour la gestion des dépendances.

### Autres changements
- Correction de typos.
- Correction d'une commande pnpm.
- Ajustement de liens internes.
- Mise à jour de plusieurs dépendances (express, brace-expansion, @lab-anssi/lib, vitest, multer, qs) via Renovate. Ces mises à jour incluent des correctifs de sécurité.
